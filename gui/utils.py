import os
import subprocess
import sys
from os.path import expanduser

from margument.yaml import read_yaml


def path_exists(path):
    if os.path.exists(path):
        return True
    return False


def list_configs():
    path = get_configs_file_path()

    if not os.path.exists(path):
        return {}

    list_of_configs = read_yaml(path)

    if list_of_configs is None or len(list_of_configs) == 0:
        return {}

    return list_of_configs


def get_configs_file_path():
    home = expanduser("~")
    return os.path.join(home, "phulize", "settings", "configs.yaml")


def open_file(path):
    if os.path.exists(path):
        subprocess.Popen(r'explorer /open,"' + path + '"')
        return True
    return False


def check_editable_config(values, value_name, window_key, to_edit, is_list=False):
    configs = list_configs()

    current_values = ''
    if len(configs) > 0:
        if is_list:
            current_values = ' '.join(configs[value_name])
        else:
            current_values = str(configs[value_name])

    input_value = values[window_key]

    if current_values != input_value:
        if is_list:
            input_value = input_value.split(' ')
        to_edit[value_name] = [input_value, is_list]


def get_icon_path():
    path = ''
    if getattr(sys, 'frozen', False):
        path = sys._MEIPASS

    ico = os.path.join(path, "icon\\logo.ico")
    return ico
