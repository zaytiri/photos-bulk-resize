import os
import subprocess
from os.path import expanduser

from gui.utils import open_file, get_configs_path


def install_program():
    print('>> '+' '.join(['pip', 'install', 'phulize']), end='\n\n')
    process = subprocess.Popen(['pip', 'install', 'phulize'], stdout=subprocess.PIPE).communicate()[0]
    print(process.decode('utf-8'))


def go_to_settings_files():
    return open_file(get_configs_path())
