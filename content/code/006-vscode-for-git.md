+++
title = "VS Code for Git"
date = 2018-09-18
slug = "vs-code-for-git"
draft = true
[taxonomies]
categories = ["Code"]
tags = ["git"]
authors = ["Luke Frisken"]
+++

My VSCode gitlens and git config

``` {.json}
"git.autofetch": true,
"gitlens.hovers.currentLine.enabled": false,
"gitlens.keymap": "chorded",
"gitlens.advanced.messages": {
    "suppressCommitHasNoPreviousCommitWarning": false,
    "suppressCommitNotFoundWarning": false,
    "suppressFileNotUnderSourceControlWarning": false,
    "suppressGitVersionWarning": false,
    "suppressLineUncommittedWarning": false,
    "suppressNoRepositoryWarning": false,
    "suppressResultsExplorerNotice": false,
    "suppressShowKeyBindingsNotice": true
},

"gitlens.historyExplorer.enabled": true,
"gitlens.hovers.currentLine.over": "line",
"gitlens.codeLens.enabled": false,
"gitlens.currentLine.enabled": false,

"terminal.integrated.shell.windows": "C:\\Program Files\\Git\\bin\\bash.exe",
```
