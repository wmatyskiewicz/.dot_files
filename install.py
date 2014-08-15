from subprocess import call

def _packages_from_file(file_name):
    _file = open(file_name)
    packages = _file.readlines()
    _file.close()
    return packages


def _task_header(str):
   color = '\033[95m'
   end = '\033[0m'
   task = '{}{:^80}{}'.format(color, str, end)
   print(task)


def install_brew():
    _task_header('Install homebrew')
    call('ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"', shell=True)


def install_brew_packages():
    _task_header('Install brew packages')
    for package in _packages_from_file('./system/.brew'):
	shell_command = 'brew install {}'.format(package)
	call(shell_command, shell=True)


def install_ohmyzsh():
    _task_header('Install oh-my-zsh')
    call('curl -L http://install.ohmyz.sh | sh', shell=True)


def config_workspace():
    _task_header('Configure Workspace')
    call('rm ../.zshrc', shell=True)
    call('ln -s .dot_files/system/.zshrc ../.zshrc', shell=True)
    call('mkdir Workspace', shell=True)
    call('sudo easy_install pip', shell=True)


def configure_sublime():
    _task_header('Configure Sublime')
    call('rm -rf ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User', shell=True)
    call('ln -s ~/.dot_files/sublime/User ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/User', shell=True)


def configure_git():
    _task_header('Configure git')   
    call('ln -s ~/.dot_files/git/.gitconfig ~/.gitconfig', shell=True)


def install_python_packages():
    _task_header('Install python packages')
    for package in _packages_from_file('./system/.python'):
        shell_command = 'sudo pip install {}'.format(package)
        call(shell_command, shell=True)

install_brew()
install_brew_packages()
install_ohmyzsh()
config_workspace()
configure_sublime()
configure_git()
install_python_packages()
