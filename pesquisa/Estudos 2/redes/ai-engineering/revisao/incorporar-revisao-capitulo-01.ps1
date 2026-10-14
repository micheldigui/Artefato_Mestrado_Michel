[CmdletBinding()]
param(
    [string]$ArtifactPath = ""
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$reviewRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$networkRoot = Split-Path -Parent $reviewRoot
$conceptRoot = Join-Path $networkRoot "conceitos"
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

if ([string]::IsNullOrWhiteSpace($ArtifactPath)) {
    $ArtifactPath = Join-Path $reviewRoot "repeticoes\ai-engineering--engenharia-de-ia--0eda37ad474f.txt"
}

$artifactFullPath = [System.IO.Path]::GetFullPath($ArtifactPath)
if (-not (Test-Path -LiteralPath $artifactFullPath -PathType Leaf)) {
    throw "Artefato de revisao nao encontrado: $artifactFullPath"
}

function ConvertTo-Slug {
    param(
        [string]$Value
    )

    $normalized = $Value.Normalize([System.Text.NormalizationForm]::FormD)
    $normalized = [regex]::Replace($normalized, '\p{Mn}', '')
    $normalized = $normalized.ToLowerInvariant()
    $normalized = [regex]::Replace($normalized, '[^a-z0-9]+', '-')
    return $normalized.Trim('-')
}

function Get-CandidateBody {
    param(
        [string]$ReviewBody
    )

    $startMarker = "## Nota candidata recebida"
    $endMarker = "## Pergunta para a segunda analise"
    $start = $ReviewBody.IndexOf($startMarker)
    if ($start -lt 0) {
        throw "Marcador de nota candidata nao encontrado no artefato."
    }

    $start = $ReviewBody.IndexOf("`n", $start)
    if ($start -lt 0) {
        throw "Corpo da nota candidata nao encontrado no artefato."
    }
    $start++

    $end = $ReviewBody.IndexOf($endMarker, $start)
    if ($end -lt 0) {
        throw "Marcador final da nota candidata nao encontrado no artefato."
    }

    return $ReviewBody.Substring($start, $end - $start).Trim()
}

function Get-NoteBlocks {
    param(
        [string]$Text
    )

    $matches = [regex]::Matches($Text, '(?m)^#\s+(.+?)\s*$')
    $notes = @()

    for ($index = 0; $index -lt $matches.Count; $index++) {
        $match = $matches[$index]
        $end = if ($index -lt ($matches.Count - 1)) {
            $matches[$index + 1].Index
        }
        else {
            $Text.Length
        }

        $body = $Text.Substring($match.Index, $end - $match.Index).Trim()
        $title = [regex]::Replace($match.Groups[1].Value.Trim(), '^[^\p{L}\p{N}]+', '')
        $notes += [pscustomobject]@{
            Title = $title.Trim()
            Slug = ConvertTo-Slug -Value $title
            Body = $body
        }
    }

    return $notes
}

function Get-SectionBlocks {
    param(
        [string]$Text
    )

    $matches = [regex]::Matches($Text, '(?m)^##\s+(.+?)\s*$')
    $sections = @{}
    for ($index = 0; $index -lt $matches.Count; $index++) {
        $match = $matches[$index]
        $end = if ($index -lt ($matches.Count - 1)) {
            $matches[$index + 1].Index
        }
        else {
            $Text.Length
        }

        $body = $Text.Substring($match.Index, $end - $match.Index).Trim()
        $key = ConvertTo-Slug -Value $match.Groups[1].Value.Trim()
        $sections[$key] = [pscustomobject]@{
            Key = $key
            Body = $body
            Length = $body.Length
        }
    }

    return $sections
}

function Get-ConceptFileIndex {
    param(
        [string]$Path
    )

    $index = @{}
    foreach ($file in (Get-ChildItem -LiteralPath $Path -File -Filter "*.md")) {
        $body = [System.IO.File]::ReadAllText($file.FullName, $utf8NoBom)
        $heading = [regex]::Match($body, '(?m)^#\s+(.+?)\s*$')
        if (-not $heading.Success) {
            continue
        }

        $title = [regex]::Replace($heading.Groups[1].Value.Trim(), '^[^\p{L}\p{N}]+', '')
        $key = ConvertTo-Slug -Value $title
        if ($key -and (-not $index.ContainsKey($key))) {
            $index[$key] = $file
        }
    }

    return $index
}

function Merge-Note {
    param(
        [string]$CandidateBody,
        [string]$CurrentBody
    )

    $candidateSections = Get-SectionBlocks -Text $CandidateBody
    $currentSections = Get-SectionBlocks -Text $CurrentBody
    $candidateHeadings = [regex]::Matches($CandidateBody, '(?m)^##\s+(.+?)\s*$')

    if ($candidateHeadings.Count -eq 0) {
        return $CandidateBody
    }

    $preamble = $CandidateBody.Substring(0, $candidateHeadings[0].Index).TrimEnd()
    $parts = @($preamble)

    foreach ($heading in $candidateHeadings) {
        $key = ConvertTo-Slug -Value $heading.Groups[1].Value.Trim()
        $section = $candidateSections[$key]
        $selectedBody = $section.Body

        if ($currentSections.ContainsKey($key)) {
            $currentSection = $currentSections[$key]
            if (($key -eq "notas-pessoais") -or ($currentSection.Length -gt $section.Length)) {
                $selectedBody = $currentSection.Body
            }
        }

        $parts += $selectedBody
    }

    $merged = ($parts -join [Environment]::NewLine + [Environment]::NewLine).Trim()

    $linkReplacements = @{
        'redes/ai-engineering/conceitos/geracao-aumentada-de-recuperacao.md' = 'redes/ai-engineering/conceitos/rag.md'
        'redes/ai-engineering/conceitos/ajuste-fino.md' = 'redes/ai-engineering/conceitos/finetuning.md'
        'redes/ai-engineering/conceitos/humano-no-loop.md' = 'redes/ai-engineering/conceitos/humano-no-loop-crawl-walk-run.md'
    }

    foreach ($oldPath in $linkReplacements.Keys) {
        $merged = $merged.Replace($oldPath, $linkReplacements[$oldPath])
    }

    return $merged
}

$reviewBody = [System.IO.File]::ReadAllText($artifactFullPath, $utf8NoBom)
$candidateBody = Get-CandidateBody -ReviewBody $reviewBody
$candidateNotes = @(Get-NoteBlocks -Text $candidateBody)
$conceptIndex = Get-ConceptFileIndex -Path $conceptRoot
$updated = 0
$unchanged = 0

foreach ($candidate in $candidateNotes) {
    $targetFile = $null
    if ($candidate.Slug -eq "geracao-aumentada-de-recuperacao-rag") {
        $targetFile = Join-Path $conceptRoot "rag.md"
    }
    elseif ($conceptIndex.ContainsKey($candidate.Slug)) {
        $targetFile = $conceptIndex[$candidate.Slug].FullName
    }

    if ([string]::IsNullOrWhiteSpace($targetFile) -or (-not (Test-Path -LiteralPath $targetFile -PathType Leaf))) {
        Write-Warning "Nota sem arquivo canonico correspondente: $($candidate.Title)"
        continue
    }

    $currentBody = [System.IO.File]::ReadAllText($targetFile, $utf8NoBom)
    $mergedBody = Merge-Note -CandidateBody $candidate.Body -CurrentBody $currentBody

    if ($mergedBody -eq $currentBody.Trim()) {
        $unchanged++
        continue
    }

    [System.IO.File]::WriteAllText($targetFile, $mergedBody + [Environment]::NewLine, $utf8NoBom)
    $updated++
    Write-Output "[UPDATE] $([System.IO.Path]::GetFileName($targetFile))"
}

Write-Output "[OK] Notas candidatas analisadas: $($candidateNotes.Count)"
Write-Output "[OK] Notas canonicas atualizadas: $updated"
Write-Output "[OK] Notas sem alteracao: $unchanged"
Write-Output "[OK] Artefato usado: $artifactFullPath"
