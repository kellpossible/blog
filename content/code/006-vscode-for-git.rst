Javadoc's inheritDoc
=========================================

:date: 2018-09-18 20:00
:author: Luke Frisken
:slug: code/vscode-for-git
:image: {photo}/.jpg
:dropcap:
:status: draft

My VSCode gitlens and git config

.. code-block:: json

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