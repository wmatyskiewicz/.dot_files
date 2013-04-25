ZSH=$HOME/.oh-my-zsh
ZSH_THEME="af-magic"

plugins=(git python pip redis-cli screen forklift sublime)

compctl -/ -W ~/Workspace project

source $ZSH/oh-my-zsh.sh
source ~/.workspace_config/.aliases

export PATH=/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/local/git/bin
