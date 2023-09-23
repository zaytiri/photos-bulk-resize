import os

import argparse
from os.path import expanduser

from margument.non_repeatable_settings import NonRepeatableSettings
from margument.options import Options
from margument.settings_processor import SettingsProcessor
from phulize.settings.settings import Settings
from phulize.version.progsettings import get_version


def get_path():
    home = expanduser("~")
    path = os.path.join(home, 'phulize')
    if not os.path.exists(path):
        os.mkdir(path)
    final_path = os.path.join(path, 'settings')
    if not os.path.exists(final_path):
        os.mkdir(final_path)
    return final_path


class Manager:
    def __init__(self):
        self.args = argparse.ArgumentParser()
        self.args.add_argument('--version', action='version', version='%(prog)s ' + str(get_version()))

    def configure_arguments(self, custom_args=None, is_gui=False):
        # manage generic configurations
        custom_settings = Settings()
        custom_settings.set_is_gui(is_gui)

        settings = NonRepeatableSettings(path=os.path.join(get_path(), 'configs.yaml'),
                                         program_arguments=custom_settings,
                                         options=Options(show_saved=True, save_different=True))

        settings_processor = SettingsProcessor([settings], self.args)

        return settings_processor.run(custom_args=custom_args)
