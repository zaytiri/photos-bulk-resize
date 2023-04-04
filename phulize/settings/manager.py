import os

import argparse

from margument.non_repeatable_settings import NonRepeatableSettings
from margument.options import Options
from margument.settings_processor import SettingsProcessor
from phulize.settings.settings import Settings
from phulize.version.progsettings import get_version


class Manager:
    def __init__(self):
        self.args = argparse.ArgumentParser()
        self.args.add_argument('--version', action='version', version='%(prog)s ' + str(get_version()))

    def configure_arguments(self):
        # manage generic configurations
        settings = NonRepeatableSettings(path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'configs.yaml'),
                                         program_arguments=Settings(),
                                         options=Options(show_saved=True, save_different=True))

        settings_processor = SettingsProcessor([settings], self.args)

        return settings_processor.run()
