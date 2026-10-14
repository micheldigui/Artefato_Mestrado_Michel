[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$reviewRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$networkRoot = Split-Path -Parent $reviewRoot
$vaultRoot = Split-Path -Parent (Split-Path -Parent $networkRoot)
$aiConceptRoot = Join-Path $networkRoot "conceitos"
$mlRoot = Join-Path $vaultRoot "redes\machine-learning"
$mlConceptRoot = Join-Path $mlRoot "conceitos"
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

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

function Get-ConceptIndex {
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
        $keys = @(
            (ConvertTo-Slug -Value $title),
            (ConvertTo-Slug -Value $file.BaseName)
        ) | Where-Object { $_ } | Sort-Object -Unique

        foreach ($key in $keys) {
            if (-not $index.ContainsKey($key)) {
                $relativePath = $file.FullName.Replace($vaultRoot.TrimEnd('\') + '\', '').Replace('\', '/')
                $index[$key] = [pscustomobject]@{
                    Path = $relativePath
                    Title = $title
                }
            }
        }
    }

    return $index
}

function New-ConnectionSection {
    param(
        [string[]]$ConceptSlugs,
        [hashtable]$MachineLearningIndex
    )

    $lines = @(
        "## Conexoes com Machine Learning",
        "",
        "Estes fundamentos pertencem a outra rede e foram ligados como prerequisitos ou conceitos vizinhos. O MOC nao e usado como no conceitual."
    )

    foreach ($slug in $ConceptSlugs) {
        if (-not $MachineLearningIndex.ContainsKey($slug)) {
            throw "Conceito de Machine Learning nao encontrado: $slug"
        }

        $concept = $MachineLearningIndex[$slug]
        $lines += "- [[$($concept.Path)|$($concept.Title)]]"
    }

    return ($lines -join [Environment]::NewLine)
}

function Set-ConnectionSection {
    param(
        [string]$Body,
        [string]$Section
    )

    $sectionPattern = '(?ms)^##\s+Conexoes com Machine Learning\s*\r?\n.*?(?=^##\s+|\z)'
    if ([regex]::IsMatch($Body, $sectionPattern)) {
        return [regex]::Replace($Body, $sectionPattern, $Section.Trim() + [Environment]::NewLine + [Environment]::NewLine)
    }

    $personalHeading = [regex]::Match($Body, '(?m)^##\s+.*Notas pessoais.*$')
    if ($personalHeading.Success) {
        $before = $Body.Substring(0, $personalHeading.Index).TrimEnd()
        $after = $Body.Substring($personalHeading.Index).TrimStart()
        return $before + [Environment]::NewLine + [Environment]::NewLine + $Section.Trim() + [Environment]::NewLine + [Environment]::NewLine + $after
    }

    return $Body.TrimEnd() + [Environment]::NewLine + [Environment]::NewLine + $Section.Trim()
}

if (-not (Test-Path -LiteralPath $aiConceptRoot -PathType Container)) {
    throw "Pasta de conceitos de AI Engineering nao encontrada: $aiConceptRoot"
}
if (-not (Test-Path -LiteralPath $mlConceptRoot -PathType Container)) {
    throw "Pasta de conceitos de Machine Learning nao encontrada: $mlConceptRoot"
}

$machineLearningIndex = Get-ConceptIndex -Path $mlConceptRoot

$mapping = [ordered]@{
    "engenharia-de-ia.md" = @("deep-learning-redes-neurais", "overfitting-e-underfitting", "cross-validation")
    "modelo-de-fundacao.md" = @("deep-learning-redes-neurais", "redes-neurais-artificiais", "backpropagation")
    "modelo-de-linguagem.md" = @("deep-learning-redes-neurais", "redes-neurais-artificiais", "backpropagation", "funcoes-de-ativacao")
    "auto-supervisao.md" = @("deep-learning-redes-neurais", "redes-neurais-artificiais", "overfitting-e-underfitting")
    "mecanismo-de-atencao.md" = @("deep-learning-redes-neurais", "redes-neurais-artificiais", "funcoes-de-ativacao")
    "finetuning.md" = @("gradient-descent", "loss-functions", "regularizacao-l1-lasso", "regularizacao-l2-ridge", "overfitting-e-underfitting")
    "data-centric-ai.md" = @("feature-engineering", "imbalanced-data", "outliers", "normalizacao-e-padronizacao", "tratamento-de-missing-values", "selecao-de-atributos-feature-selection")
    "desenvolvimento-orientado-por-avaliacao.md" = @("cross-validation", "bias-variance-tradeoff", "matriz-de-confusao", "roc-auc", "precision-e-recall", "f1-score", "rmse-e-mae")
    "desafios-de-avaliacao-de-modelos-de-fundacao.md" = @("cross-validation", "bias-variance-tradeoff", "matriz-de-confusao", "roc-auc", "precision-e-recall", "f1-score", "rmse-e-mae")
}

$updated = 0
$unchanged = 0

foreach ($fileName in $mapping.Keys) {
    $targetPath = Join-Path $aiConceptRoot $fileName
    if (-not (Test-Path -LiteralPath $targetPath -PathType Leaf)) {
        throw "Nota de AI Engineering nao encontrada: $targetPath"
    }

    $body = [System.IO.File]::ReadAllText($targetPath, $utf8NoBom)
    $section = New-ConnectionSection -ConceptSlugs $mapping[$fileName] -MachineLearningIndex $machineLearningIndex
    $updatedBody = Set-ConnectionSection -Body $body -Section $section

    if ($updatedBody -eq $body) {
        $unchanged++
        continue
    }

    [System.IO.File]::WriteAllText($targetPath, $updatedBody.Trim() + [Environment]::NewLine, $utf8NoBom)
    $updated++
    Write-Output "[UPDATE] $fileName"
}

Write-Output "[OK] Notas atualizadas: $updated"
Write-Output "[OK] Notas sem alteracao: $unchanged"
Write-Output "[OK] Conexoes adicionadas sem usar o MOC como no"
