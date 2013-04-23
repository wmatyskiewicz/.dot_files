ZSH=$HOME/.oh-my-zsh
ZSH_THEME="af-magic"

plugins=(git python pip redis-cli screen forklift sublime)

source $ZSH/oh-my-zsh.sh

# Sys aliases
alias ll="ls -al"

# Workspace aliases
function cdproject
{
	cd ~/Workspace/$1/
}

alias workspace="cd ~/Workspace"
alias project=cdproject

# Python aliases
function activateenv
{
	source ~/Workspace/$1/bin/activate
	cd ~/Workspace/$1/
}

alias makeenv="~/.workspace_config/scripts/python-env.sh"
alias activateenv=activateenv
alias clearenv="find . -name '*.pyc' -delete"

export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/git/bin
