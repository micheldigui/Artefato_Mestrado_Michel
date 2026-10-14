[CmdletBinding()]
param(
    [string]$InputFile = "",
    [string]$InputRoot = "",
    [string]$VaultRoot = "",
    [string]$ReviewRoot = "",
    [switch]$Overwrite,
    [switch]$Reprocess
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path

if ([string]::IsNullOrWhiteSpace($VaultRoot)) {
    $VaultRoot = Join-Path $scriptDir "..\..\.."
}

$vaultFullPath = [System.IO.Path]::GetFullPath($VaultRoot)
$statePath = Join-Path $scriptDir ".split_obsidian_state.json"
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$parserVersion = 3

if ([string]::IsNullOrWhiteSpace($ReviewRoot)) {
    $networkRoot = Split-Path -Parent $scriptDir
    $ReviewRoot = Join-Path $networkRoot "revisao\repeticoes"
}

$reviewFullPath = [System.IO.Path]::GetFullPath($ReviewRoot)
$duplicateLogPath = Join-Path (Split-Path -Parent $reviewFullPath) "repeticoes.log"
$validationFilePath = Join-Path (Split-Path -Parent $reviewFullPath) "validacao-ia-repeticoes.txt"

if (-not (Test-Path -LiteralPath $vaultFullPath -PathType Container)) {
    throw "Raiz do vault nao encontrada: $vaultFullPath"
}

function Get-CompiledBlocks {
    param(
        [string]$Text
    )

    $markerPattern = '(?m)^[ \t]*\\?===ARQUIVO:\s*(?<path>.+?)===\s*$'
    $markerMatches = [regex]::Matches($Text, $markerPattern)

    if ($markerMatches.Count -eq 0) {
        return $null
    }

    $blocks = @()

    for ($index = 0; $index -lt $markerMatches.Count; $index++) {
        $marker = $markerMatches[$index]
        $relativeTarget = $marker.Groups["path"].Value.Trim()
        $bodyStart = $marker.Index + $marker.Length

        if ($index -lt ($markerMatches.Count - 1)) {
            $bodyEnd = $markerMatches[$index + 1].Index
        }
        else {
            $bodyEnd = $Text.Length
        }

        $body = $Text.Substring($bodyStart, $bodyEnd - $bodyStart).Trim()
        $body = [regex]::Replace($body, '^```[ \t]*(markdown|md|json|yaml|text)?[ \t]*\r?\n', '')
        $body = [regex]::Replace($body, '\r?\n```[ \t]*$', '')
        $body = $body.Trim()

        $isCanonicalReference = ($body -match '^\(Conceito') -and ($body -match 'criado anteriormente')

        $blocks += [pscustomobject]@{
            Target = $relativeTarget
            Body = $body
            IsCanonicalReference = $isCanonicalReference
        }
    }

    return [pscustomobject]@{
        Count = $markerMatches.Count
        Blocks = $blocks
    }
}

function Get-TargetPath {
    param(
        [string]$RelativeTarget,
        [string]$VaultPath
    )

    $normalizedTarget = $RelativeTarget.Replace('/', [System.IO.Path]::DirectorySeparatorChar)

    if ([System.IO.Path]::IsPathRooted($normalizedTarget)) {
        throw "Caminho absoluto nao permitido: $RelativeTarget"
    }

    $segments = $normalizedTarget -split '[\\/]'
    if ($segments -contains '..') {
        throw "Caminho fora do vault nao permitido: $RelativeTarget"
    }

    $destination = [System.IO.Path]::GetFullPath((Join-Path $VaultPath $normalizedTarget))
    $vaultPrefix = $VaultPath.TrimEnd([System.IO.Path]::DirectorySeparatorChar, [System.IO.Path]::AltDirectorySeparatorChar) + [System.IO.Path]::DirectorySeparatorChar

    if (-not $destination.StartsWith($vaultPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Caminho fora do vault nao permitido: $RelativeTarget"
    }

    return $destination
}

function Get-LogicalTargetKey {
    param(
        [string]$Target
    )

    $key = $Target.Normalize([System.Text.NormalizationForm]::FormD)
    $key = [regex]::Replace($key, '\p{Mn}', '')
    return $key.ToLowerInvariant()
}

function Get-ConceptKey {
    param(
        [string]$Value
    )

    if ([string]::IsNullOrWhiteSpace($Value)) {
        return ""
    }

    $key = Get-LogicalTargetKey -Target $Value
    $key = [regex]::Replace($key, '[^a-z0-9]+', '-')
    return $key.Trim('-')
}

function Expand-ConceptBlock {
    param(
        [pscustomobject]$Block
    )

    if ($Block.Target -notmatch '(^|[/\\])conceitos([/\\])') {
        return @($Block)
    }

    $headingPattern = '(?m)^#\s+(.+?)\s*$'
    $headingMatches = [regex]::Matches($Block.Body, $headingPattern)
    if ($headingMatches.Count -le 1) {
        return @($Block)
    }

    $directoryMatch = [regex]::Match($Block.Target, '^(.*[/\\])')
    $targetDirectory = ""
    if ($directoryMatch.Success) {
        $targetDirectory = $directoryMatch.Groups[1].Value
    }

    $extension = [System.IO.Path]::GetExtension($Block.Target)
    if ([string]::IsNullOrWhiteSpace($extension)) {
        $extension = ".md"
    }

    $expanded = @()
    for ($index = 0; $index -lt $headingMatches.Count; $index++) {
        $heading = $headingMatches[$index]
        $bodyStart = $heading.Index

        if ($index -lt ($headingMatches.Count - 1)) {
            $bodyEnd = $headingMatches[$index + 1].Index
        }
        else {
            $bodyEnd = $Block.Body.Length
        }

        $body = $Block.Body.Substring($bodyStart, $bodyEnd - $bodyStart).Trim()
        $title = $heading.Groups[1].Value.Trim()
        $slug = Get-ConceptKey -Value $title
        if ([string]::IsNullOrWhiteSpace($slug)) {
            throw "Nao foi possivel gerar um nome de arquivo para o conceito '$title' em '$($Block.Target)'."
        }

        $expanded += [pscustomobject]@{
            Target = $targetDirectory + $slug + $extension
            Body = $body
            IsCanonicalReference = $false
            WasExpanded = $true
            OriginalTarget = $Block.Target
        }
    }

    return $expanded
}

function Get-ConceptTitle {
    param(
        [string]$Body
    )

    $frontmatterTitle = [regex]::Match($Body, '(?m)^title:\s*"?([^"\r\n]+)"?\s*$')
    if ($frontmatterTitle.Success) {
        return $frontmatterTitle.Groups[1].Value.Trim()
    }

    $heading = [regex]::Match($Body, '(?m)^#\s+(.+?)\s*$')
    if ($heading.Success) {
        $title = [regex]::Replace($heading.Groups[1].Value.Trim(), '^[^\p{L}\p{N}]+', '')
        return $title.Trim()
    }

    return ""
}

function Get-ConceptKeys {
    param(
        [string]$Title,
        [string]$Target
    )

    $values = @($Title, $Target)
    $keys = @()

    foreach ($value in $values) {
        $key = Get-ConceptKey -Value $value
        if ($key) {
            $keys += $key
        }

        foreach ($aliasMatch in [regex]::Matches($value, '\(([^\)]+)\)')) {
            $aliasKey = Get-ConceptKey -Value $aliasMatch.Groups[1].Value
            if ($aliasKey) {
                $keys += $aliasKey
            }
        }
    }

    return @($keys | Sort-Object -Unique)
}

function Get-ConceptAliases {
    param(
        [string]$Body
    )

    $aliases = @()
    $match = [regex]::Match($Body, '(?ms)^aliases:\s*(.*?)(?=^\w[\w_-]*:|\z)')
    if ($match.Success) {
        foreach ($line in ($match.Groups[1].Value -split "`r?`n")) {
            $aliasMatch = [regex]::Match($line, '^\s*-\s*"?([^"\r\n]+)"?\s*$')
            if ($aliasMatch.Success) {
                $aliases += $aliasMatch.Groups[1].Value.Trim()
            }
        }
    }

    return @($aliases)
}

function Get-ConceptIndex {
    param(
        [string]$ConceptPath,
        [string]$VaultPath
    )

    $index = @{}
    foreach ($file in (Get-ChildItem -LiteralPath $ConceptPath -Recurse -File -Filter "*.md")) {
        $body = [System.IO.File]::ReadAllText($file.FullName, $utf8NoBom)
        if ($null -ne (Get-CompiledBlocks -Text $body)) {
            continue
        }

        $title = Get-ConceptTitle -Body $body
        $keys = @(Get-ConceptKeys -Title $title -Target $file.BaseName)
        foreach ($alias in (Get-ConceptAliases -Body $body)) {
            $aliasKey = Get-ConceptKey -Value $alias
            if ($aliasKey) {
                $keys += $aliasKey
            }
        }

        $relativePath = $file.FullName.Replace($VaultPath.TrimEnd('\') + '\', '')
        foreach ($key in ($keys | Sort-Object -Unique)) {
            if ($key -and (-not $index.ContainsKey($key))) {
                $index[$key] = [pscustomobject]@{
                    Path = $file.FullName
                    RelativePath = $relativePath
                    Title = $title
                }
            }
        }
    }

    return $index
}

function Find-ConceptDuplicate {
    param(
        [pscustomobject]$Block,
        [hashtable]$ConceptIndex,
        [string]$VaultPath
    )

    if ($Block.Target -notmatch '(^|[/\\])conceitos([/\\])') {
        return $null
    }

    $targetFile = [System.IO.Path]::GetFileNameWithoutExtension($Block.Target)
    $title = Get-ConceptTitle -Body $Block.Body
    $keys = @(Get-ConceptKeys -Title $title -Target $targetFile)

    foreach ($key in $keys) {
        if ($ConceptIndex.ContainsKey($key)) {
            $match = $ConceptIndex[$key]
            return [pscustomobject]@{
                CanonicalPath = $match.RelativePath
                CanonicalTitle = $match.Title
                Reason = "titulo, alias ou slug equivalente: $key"
            }
        }
    }

    $destination = Get-TargetPath -RelativeTarget $Block.Target -VaultPath $VaultPath
    if (Test-Path -LiteralPath $destination -PathType Leaf) {
        return [pscustomobject]@{
            CanonicalPath = $Block.Target
            CanonicalTitle = $title
            Reason = "arquivo de destino ja existe"
        }
    }

    return $null
}

function Write-DuplicateReview {
    param(
        [string]$ReviewPath,
        [string]$SourceFile,
        [string]$SourceHash,
        [string]$IncomingTarget,
        [pscustomobject]$Duplicate,
        [string]$Body,
        [switch]$OverwriteExisting,
        [System.Text.UTF8Encoding]$Encoding
    )

    if ((Test-Path -LiteralPath $ReviewPath -PathType Leaf) -and (-not $OverwriteExisting)) {
        return $false
    }

    $safeSourceFile = $SourceFile.Replace("'", "''")
    $safeSourceHash = $SourceHash.Replace("'", "''")
    $safeIncomingTarget = $IncomingTarget.Replace("'", "''")
    $safeCanonicalPath = $Duplicate.CanonicalPath.Replace("'", "''")
    $safeReason = $Duplicate.Reason.Replace("'", "''")
    $content = @(
        '---',
        'type: "revisao-repeticao"',
        'status: "aguardando-analise"',
        "source_file: '$safeSourceFile'",
        "source_hash: '$safeSourceHash'",
        "incoming_target: '$safeIncomingTarget'",
        "canonical_path: '$safeCanonicalPath'",
        "duplicate_reason: '$safeReason'",
        '---',
        '',
        '# Revisao de conceito repetido',
        '',
        '## Nota candidata recebida',
        '',
        $Body,
        '',
        '## Pergunta para a segunda analise',
        '',
        'Compare esta nota com a nota canonica indicada no frontmatter. Extraia somente informacoes novas, corrija divergencias e proponha atualizacoes sem duplicar o conceito.',
        ''
    )

    $parent = Split-Path -Parent $ReviewPath
    New-Item -ItemType Directory -Path $parent -Force | Out-Null
    [System.IO.File]::WriteAllText($ReviewPath, ($content -join [Environment]::NewLine), $Encoding)
    return $true
}

function Read-DuplicateLogKeys {
    param(
        [string]$Path
    )

    $keys = @{}
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return $keys
    }

    foreach ($line in (Get-Content -LiteralPath $Path -Encoding utf8)) {
        if ([string]::IsNullOrWhiteSpace($line)) {
            continue
        }
        try {
            $record = $line | ConvertFrom-Json
            if ($record.key) {
                $keys[$record.key] = $true
            }
        }
        catch {
            continue
        }
    }

    return $keys
}

function Add-DuplicateLog {
    param(
        [hashtable]$SeenKeys,
        [string]$Path,
        [string]$Key,
        [string]$SourceFile,
        [string]$IncomingTarget,
        [pscustomobject]$Duplicate,
        [string]$ReviewPath,
        [System.Text.UTF8Encoding]$Encoding
    )

    if ($SeenKeys.ContainsKey($Key)) {
        return $false
    }

    $record = [ordered]@{
        key = $Key
        detected_at = (Get-Date).ToString("o")
        source_file = $SourceFile
        incoming_target = $IncomingTarget
        canonical_path = $Duplicate.CanonicalPath
        reason = $Duplicate.Reason
        review_artifact = $ReviewPath
        status = "aguardando-analise"
    }

    $line = $record | ConvertTo-Json -Compress -Depth 5
    $parent = Split-Path -Parent $Path
    New-Item -ItemType Directory -Path $parent -Force | Out-Null
    [System.IO.File]::AppendAllText($Path, $line + [Environment]::NewLine, $Encoding)
    $SeenKeys[$Key] = $true
    return $true
}

function Get-FrontmatterValue {
    param(
        [string]$Body,
        [string]$Name
    )

    $pattern = '(?m)^' + [regex]::Escape($Name) + ':\s*["'']?([^"''\r\n]+)["'']?\s*$'
    $match = [regex]::Match($Body, $pattern)
    if ($match.Success) {
        return $match.Groups[1].Value.Trim()
    }

    return ""
}

function Get-ReviewCandidateBody {
    param(
        [string]$ReviewBody
    )

    $startMarker = "## Nota candidata recebida"
    $endMarker = "## Pergunta para a segunda analise"
    $start = $ReviewBody.IndexOf($startMarker)
    if ($start -lt 0) {
        return $ReviewBody
    }

    $start = $ReviewBody.IndexOf("`n", $start)
    if ($start -lt 0) {
        return ""
    }
    $start++
    $end = $ReviewBody.IndexOf($endMarker, $start)
    if ($end -lt 0) {
        $end = $ReviewBody.Length
    }

    return $ReviewBody.Substring($start, $end - $start).Trim()
}

function Write-AiValidationPackage {
    param(
        [string]$ReviewPath,
        [string]$ValidationPath,
        [string]$VaultPath,
        [System.Text.UTF8Encoding]$Encoding
    )

    $reviews = @(Get-ChildItem -LiteralPath $ReviewPath -File | Where-Object { $_.Extension -in @(".txt", ".md") } | Sort-Object Name)
    $lines = @(
        '# Pacote de validacao de conceitos repetidos',
        '',
        'Este arquivo reune notas candidatas que foram identificadas como repetidas de conceitos canonicos.',
        'A nota canonica deve ser preservada. A analise deve extrair apenas informacoes novas ou correcoes.',
        '',
        '## Prompt para a IA',
        '',
        'Compare cada nota candidata com a nota canonica indicada.',
        'Nao reescreva a nota inteira.',
        'Nao invente fatos, fontes, paginas ou links.',
        'Se a nota candidata apenas repetir o conteudo canonico, use discard.',
        'Se houver informacao nova confiavel, use incorporate e proponha operacoes pequenas e localizadas.',
        'Se houver conflito, ambiguidade ou risco de alterar o significado, use manual_review.',
        'Retorne somente um objeto JSON valido, sem cercas Markdown e sem comentarios.',
        '',
        '## Schema obrigatorio da resposta',
        '',
        '```json',
        '{',
        '  "version": "1.0",',
        '  "decisions": [',
        '    {',
        '      "review_id": "nome-do-arquivo-de-revisao",',
        '      "canonical_path": "redes/ai-engineering/conceitos/conceito.md",',
        '      "action": "incorporate|discard|manual_review",',
        '      "confidence": "alta|media|baixa",',
        '      "reason": "explicacao curta",',
        '      "updates": [',
        '        {',
        '          "operation": "append_to_section|replace_section|add_relation",',
        '          "section": "## Nome da secao",',
        '          "target": "redes/ai-engineering/conceitos/outro-conceito.md",',
        '          "content": "texto novo ou corrigido"',
        '        }',
        '      ],',
        '      "source_evidence": {',
        '        "source_id": "...",',
        '        "chapter": "...",',
        '        "location": "...",',
        '        "summary": "parafrase fiel da evidencia"',
        '      }',
        '    }',
        '  ]',
        '}',
        '```',
        '',
        'Regras para updates:',
        '- use append_to_section somente para informacao realmente nova;',
        '- use replace_section somente quando houver erro factual claro e indique o motivo;',
        '- use add_relation apenas para links que existam no vault ou estejam entre os casos desta rodada;',
        '- para discard, mantenha updates vazio;',
        '- para manual_review, nao proponha alteracao automatica perigosa;',
        ''
    )

    $caseCount = 0
    $caseIds = @()
    foreach ($review in $reviews) {
        $reviewBody = [System.IO.File]::ReadAllText($review.FullName, $Encoding)
        $canonicalPath = Get-FrontmatterValue -Body $reviewBody -Name "canonical_path"
        $incomingTarget = Get-FrontmatterValue -Body $reviewBody -Name "incoming_target"
        $sourceFile = Get-FrontmatterValue -Body $reviewBody -Name "source_file"

        if ([string]::IsNullOrWhiteSpace($canonicalPath)) {
            continue
        }

        $canonicalFullPath = Get-TargetPath -RelativeTarget $canonicalPath -VaultPath $VaultPath
        $canonicalBody = "[Nota canonica nao encontrada: $canonicalPath]"
        if (Test-Path -LiteralPath $canonicalFullPath -PathType Leaf) {
            $canonicalBody = [System.IO.File]::ReadAllText($canonicalFullPath, $Encoding)
        }

        $candidateBody = Get-ReviewCandidateBody -ReviewBody $reviewBody
        $caseCount++
        $caseIds += $review.BaseName
        $canonicalPathDisplay = $canonicalPath.Replace('\', '/')
        $lines += "### CASO ${caseCount}: $($review.BaseName)"
        $lines += ""
        $lines += "review_id: $($review.BaseName)"
        $lines += "source_file: $sourceFile"
        $lines += "incoming_target: $incomingTarget"
        $lines += "canonical_path: $canonicalPathDisplay"
        $lines += ""
        $lines += "#### NOTA CANONICA"
        $lines += ""
        $lines += '````markdown'
        $lines += ($canonicalBody -split "`r?`n")
        $lines += '````'
        $lines += ""
        $lines += "#### NOTA CANDIDATA REPETIDA"
        $lines += ""
        $lines += '````markdown'
        $lines += ($candidateBody -split "`r?`n")
        $lines += '````'
        $lines += ""
    }

    $lines += '## Contrato de cobertura'
    $lines += ''
    $lines += "A resposta deve conter exatamente $caseCount objeto(s) em decisions, um para cada review_id abaixo."
    $lines += 'Nao omita casos e nao crie review_id que nao esteja nesta lista.'
    $lines += ''
    foreach ($caseId in $caseIds) {
        $lines += "- $caseId"
    }
    $lines += ''
    $lines += 'Use caminhos relativos ao vault com barras normais (/).'
    $lines += 'Nao inclua texto antes ou depois do objeto JSON.'
    $lines += ''
    $lines += "## Total de casos: $caseCount"
    New-Item -ItemType Directory -Path (Split-Path -Parent $ValidationPath) -Force | Out-Null
    [System.IO.File]::WriteAllText($ValidationPath, ($lines -join [Environment]::NewLine) + [Environment]::NewLine, $Encoding)
    return $caseCount
}

function Read-State {
    param(
        [string]$Path
    )

    $state = @{}

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return $state
    }

    try {
        $rawState = [System.IO.File]::ReadAllText($Path, $utf8NoBom) | ConvertFrom-Json
        if ($null -ne $rawState.files) {
            foreach ($property in $rawState.files.PSObject.Properties) {
                $state[$property.Name] = $property.Value
            }
        }
    }
    catch {
        Write-Warning "Estado invalido ou ilegivel. Um novo estado sera criado: $Path"
    }

    return $state
}

function Write-State {
    param(
        [hashtable]$State,
        [string]$Path,
        [System.Text.UTF8Encoding]$Encoding
    )

    $files = [ordered]@{}
    foreach ($key in ($State.Keys | Sort-Object)) {
        $files[$key] = $State[$key]
    }

    $payload = [ordered]@{
        version = 2
        files = $files
    }

    $json = $payload | ConvertTo-Json -Depth 10
    [System.IO.File]::WriteAllText($Path, $json + [Environment]::NewLine, $Encoding)
}

if ((-not [string]::IsNullOrWhiteSpace($InputFile)) -and (-not [string]::IsNullOrWhiteSpace($InputRoot))) {
    throw "Use apenas um modo de entrada: -InputFile ou -InputRoot."
}

$inputMode = "pasta padrao"
$inputLocation = $scriptDir

if (-not [string]::IsNullOrWhiteSpace($InputFile)) {
    $inputFullPath = [System.IO.Path]::GetFullPath($InputFile)
    if (-not (Test-Path -LiteralPath $inputFullPath -PathType Leaf)) {
        throw "Arquivo de entrada nao encontrado: $inputFullPath"
    }
    $candidates = @(Get-Item -LiteralPath $inputFullPath)
    $inputMode = "arquivo unico"
    $inputLocation = $inputFullPath
}
elseif (-not [string]::IsNullOrWhiteSpace($InputRoot)) {
    $inputRootFullPath = [System.IO.Path]::GetFullPath($InputRoot)
    if (-not (Test-Path -LiteralPath $inputRootFullPath -PathType Container)) {
        throw "Pasta de entrada nao encontrada: $inputRootFullPath"
    }
    $candidates = @(Get-ChildItem -LiteralPath $inputRootFullPath -Recurse -File -Filter "*.md")
    $inputMode = "pasta informada"
    $inputLocation = $inputRootFullPath
}
else {
    $candidates = @(Get-ChildItem -LiteralPath $scriptDir -Recurse -File -Filter "*.md")
}

$state = Read-State -Path $statePath
$conceptIndex = Get-ConceptIndex -ConceptPath $scriptDir -VaultPath $vaultFullPath
$duplicateLogKeys = Read-DuplicateLogKeys -Path $duplicateLogPath
$compiledCount = 0
$processedCount = 0
$unchangedCount = 0
$splitCount = 0
$expandedConceptCount = 0
$referenceCount = 0
$writtenCount = 0
$duplicateCount = 0
$reviewCount = 0
$logCount = 0

foreach ($candidate in $candidates) {
    $candidatePath = [System.IO.Path]::GetFullPath($candidate.FullName)
    $text = [System.IO.File]::ReadAllText($candidatePath, $utf8NoBom)
    $parsed = Get-CompiledBlocks -Text $text

    if ($null -eq $parsed) {
        if ($inputMode -eq "arquivo unico") {
            throw "O arquivo unico nao contem marcadores ===ARQUIVO: ...===: $candidatePath"
        }
        $splitCount++
        continue
    }

    $compiledCount++
    $fileHash = (Get-FileHash -LiteralPath $candidatePath -Algorithm SHA256).Hash
    $normalizedBlocks = @()
    foreach ($block in $parsed.Blocks) {
        $expandedBlocks = @(Expand-ConceptBlock -Block $block)
        if ($expandedBlocks.Count -gt 1) {
            $expandedConceptCount += $expandedBlocks.Count
            Write-Output "[SPLIT] $($block.Target) -> $($expandedBlocks.Count) notas por titulos H1"
        }
        $normalizedBlocks += $expandedBlocks
    }

    $usableBlocks = @($normalizedBlocks | Where-Object { -not $_.IsCanonicalReference })
    $targets = @($usableBlocks | ForEach-Object { $_.Target })
    $record = $state[$candidatePath]
    $allTargetsExist = $true
    $allHandledArtifactsExist = $true
    $recordComplete = $false
    $recordParserVersion = 0

    if (($null -ne $record) -and ($record.PSObject.Properties.Name -contains "complete")) {
        $recordComplete = [bool]$record.complete
    }

    if (($null -ne $record) -and ($record.PSObject.Properties.Name -contains "parser_version")) {
        $recordParserVersion = [int]$record.parser_version
    }

    foreach ($target in $targets) {
        $destination = Get-TargetPath -RelativeTarget $target -VaultPath $vaultFullPath
        if (-not (Test-Path -LiteralPath $destination -PathType Leaf)) {
            $allTargetsExist = $false
        }
    }

    if (($null -ne $record) -and ($record.PSObject.Properties.Name -contains "handled_artifacts")) {
        foreach ($artifact in @($record.handled_artifacts)) {
            if (-not (Test-Path -LiteralPath $artifact -PathType Leaf)) {
                $allHandledArtifactsExist = $false
            }
        }
    }
    else {
        $allHandledArtifactsExist = $allTargetsExist
    }

    if ((-not $Reprocess) -and ($null -ne $record) -and $recordComplete -and ($recordParserVersion -eq $parserVersion) -and ($record.hash -eq $fileHash) -and $allHandledArtifactsExist) {
        $unchangedCount++
        Write-Output "[SKIP] Ja processado e sem alteracoes: $($candidate.Name)"
        continue
    }

    $logicalTargets = @{}
    $complete = $true
    $handledArtifacts = @()

    foreach ($block in $normalizedBlocks) {
        if ($block.IsCanonicalReference) {
            $referenceCount++
            Write-Output "[SKIP] Referencia a nota canonica: $($block.Target)"
            continue
        }

        if ([string]::IsNullOrWhiteSpace($block.Body)) {
            throw "Bloco vazio encontrado para: $($block.Target)"
        }

        $duplicate = Find-ConceptDuplicate -Block $block -ConceptIndex $conceptIndex -VaultPath $vaultFullPath
        if ($null -ne $duplicate) {
            $sourceStem = [System.IO.Path]::GetFileNameWithoutExtension($candidatePath)
            $targetStem = [System.IO.Path]::GetFileNameWithoutExtension($block.Target)
            $reviewSlug = Get-ConceptKey -Value $targetStem
            $hashSuffix = $fileHash.Substring(0, 12).ToLowerInvariant()
            $reviewName = "$sourceStem--$reviewSlug--$hashSuffix.txt"
            $reviewPath = Join-Path $reviewFullPath $reviewName
            $logKey = "$candidatePath|$fileHash|$($block.Target)"

            $reviewCreated = Write-DuplicateReview `
                -ReviewPath $reviewPath `
                -SourceFile $candidatePath `
                -SourceHash $fileHash `
                -IncomingTarget $block.Target `
                -Duplicate $duplicate `
                -Body $block.Body `
                -OverwriteExisting:$Overwrite `
                -Encoding $utf8NoBom
            if ($reviewCreated) {
                $reviewCount++
            }

            $logAdded = Add-DuplicateLog `
                -SeenKeys $duplicateLogKeys `
                -Path $duplicateLogPath `
                -Key $logKey `
                -SourceFile $candidatePath `
                -IncomingTarget $block.Target `
                -Duplicate $duplicate `
                -ReviewPath $reviewPath `
                -Encoding $utf8NoBom
            if ($logAdded) {
                $logCount++
            }

            $handledArtifacts += $reviewPath
            $duplicateCount++
            Write-Output "[DUPLICATE] $($block.Target) -> $($duplicate.CanonicalPath)"
            continue
        }

        $logicalKey = Get-LogicalTargetKey -Target $block.Target
        if ($logicalTargets.ContainsKey($logicalKey)) {
            Write-Warning "Possivel duplicata logica: '$($block.Target)' e '$($logicalTargets[$logicalKey])'"
        }
        else {
            $logicalTargets[$logicalKey] = $block.Target
        }

        $destination = Get-TargetPath -RelativeTarget $block.Target -VaultPath $vaultFullPath
        $parent = Split-Path -Parent $destination
        New-Item -ItemType Directory -Path $parent -Force | Out-Null

        if ((Test-Path -LiteralPath $destination -PathType Leaf) -and (-not $Overwrite)) {
            Write-Output "[SKIP] Destino ja existente: $($block.Target)"
            $handledArtifacts += $destination
            continue
        }

        [System.IO.File]::WriteAllText($destination, $block.Body.Trim() + [Environment]::NewLine, $utf8NoBom)
        $handledArtifacts += $destination
        $writtenCount++
        Write-Output "[WRITE] $($block.Target)"

        $newTitle = Get-ConceptTitle -Body $block.Body
        $newKeys = @(Get-ConceptKeys -Title $newTitle -Target ([System.IO.Path]::GetFileNameWithoutExtension($block.Target)))
        foreach ($newKey in $newKeys) {
            if ($newKey -and (-not $conceptIndex.ContainsKey($newKey))) {
                $conceptIndex[$newKey] = [pscustomobject]@{
                    Path = $destination
                    RelativePath = $block.Target
                    Title = $newTitle
                }
            }
        }
    }

    $state[$candidatePath] = [ordered]@{
        parser_version = $parserVersion
        hash = $fileHash
        complete = $complete
        targets = $targets
        handled_artifacts = $handledArtifacts
        processed_at = (Get-Date).ToString("o")
    }
    $processedCount++
}

Write-State -State $state -Path $statePath -Encoding $utf8NoBom

$validationCaseCount = Write-AiValidationPackage `
    -ReviewPath $reviewFullPath `
    -ValidationPath $validationFilePath `
    -VaultPath $vaultFullPath `
    -Encoding $utf8NoBom

Write-Output "[OK] Arquivos encontrados: $($candidates.Count)"
Write-Output "[OK] Modo de entrada: $inputMode"
Write-Output "[OK] Local de entrada: $inputLocation"
Write-Output "[OK] Compilados detectados: $compiledCount"
Write-Output "[OK] Processados nesta execucao: $processedCount"
Write-Output "[OK] Pulados por idempotencia: $unchangedCount"
Write-Output "[OK] Notas splitadas ignoradas: $splitCount"
Write-Output "[OK] Blocos de conceitos expandidos por H1: $expandedConceptCount"
Write-Output "[OK] Referencias canonicas ignoradas: $referenceCount"
Write-Output "[OK] Arquivos gravados: $writtenCount"
Write-Output "[OK] Duplicidades detectadas: $duplicateCount"
Write-Output "[OK] Artefatos de revisao criados: $reviewCount"
Write-Output "[OK] Registros novos no log de repeticoes: $logCount"
Write-Output "[OK] Log de repeticoes: $duplicateLogPath"
Write-Output "[OK] Casos no pacote de validacao: $validationCaseCount"
Write-Output "[OK] Pacote de validacao da IA: $validationFilePath"
