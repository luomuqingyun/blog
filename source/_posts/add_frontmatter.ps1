$postsPath = "./"
Get-ChildItem $postsPath -Filter *.md | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    if (-not $content.StartsWith('---')) {
#   {
        $title = $_.BaseName -replace '-', ' '
        $date = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $newContent = @"
---
title: $title
author: luomuqingyun
date: $date
comments: true
category:
  - 编程
tags:
  - 编程经验
excerpt:
  - 详见完整内容
---

$content
"@
        Set-Content -Path $_.FullName -Value $newContent -NoNewline
        Write-Host "已处理: $($_.Name)"
    }
}