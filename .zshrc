ZSH=$HOME/.oh-my-zsh
ZSH_THEME="af-magic"

plugins=(git python pip redis-cli screen forklift sublime)

source $ZSH/oh-my-zsh.sh

# ALiases
alias ll="ls -al"
alias envactivate="../../../bin/activate"
alias workspace="~/Workspace"
alias pyenv="~/.workspace_config/scripts/python-env.sh"

export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/git/bin
