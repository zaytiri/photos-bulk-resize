import argparse

from margument.argument import Argument
from margument.arguments import Arguments

from phulize.utils.directory import Directory
from phulize.utils.log import throw


class Settings(Arguments):
    def __init__(self):
        self.path = Argument(name='path',
                             abbreviation_name='-p',
                             full_name='--path',
                             help_message='Folder path containing all photos to be modified.',
                             metavar="",
                             to_save=True,
                             default='')

        self.extensions = Argument(name='extensions',
                                   abbreviation_name='-e',
                                   full_name='--extensions',
                                   help_message='All image extensions to search for and modify.',
                                   metavar="",
                                   to_save=True,
                                   default=[])

        self.quality = Argument(name='quality',
                                abbreviation_name='-q',
                                full_name='--quality',
                                help_message='The quality, in percentage, the image should have relative to 100% quality. For instance, '
                                             'an original image has always 100% quality, if the inserted quality is 50 than the image\'s quality is '
                                             '50% of the original 100%. Ideal percentage and default value is: between 50-60',
                                metavar="",
                                to_save=True,
                                default=50)

        self.higher = Argument(name='higher',
                               abbreviation_name='-hi',
                               full_name='--higher',
                               help_message='If different than 0 (zero), any images\' size higher than this value, will be resized using defined '
                                            'configurations. This value is in Bytes, any size value must be convert into Bytes first.',
                               metavar="",
                               to_save=True,
                               default=0)

        self.below = Argument(name='below',
                              abbreviation_name='-b',
                              full_name='--below',
                              help_message='If different than 0 (zero), any images\' size below this value, will be resized using defined '
                                           'configurations. This value is in Bytes, any size value must be convert into Bytes first.',
                              metavar="",
                              to_save=True,
                              default=0)

        self.folder = Argument(name='folder',
                               abbreviation_name='-f',
                               full_name='--folder',
                               help_message='Folder name or path to be created. All original photos are copied to this folder with the exact '
                                            'same original folder hierarchy. Default value is \'_ORIGINAL\'. If value equals \'def\', default value '
                                            'is set.',
                               metavar="",
                               to_save=True,
                               default='_ORIGINAL')

        self.safety_question = Argument(name='safety_question',
                                        abbreviation_name='',
                                        full_name='--safety-question',
                                        help_message='[WARNING: make sure the path is the correct one] Enable/disable safety question '
                                                     'regarding modifying all files inside path configured: (default is enabled).'
                                                     'True: --safety-question | False: --no-safety-question',
                                        metavar="",
                                        default=True)

        self.shutdown = Argument(name='shutdown',
                                 abbreviation_name='',
                                 full_name='--shutdown',
                                 help_message='Enable/disable if computer will shutdown when the program has ended: (default is disabled)'
                                              'True: --shutdown | False: --no-shutdown',
                                 metavar="",
                                 default=False)

        self.run = Argument(name='run',
                            abbreviation_name='-r',
                            full_name='--run',
                            help_message='If specified, it will start the resizing process with configured settings.',
                            metavar="",
                            default=False)

    def add_arguments(self, args_parser):
        args_parser.add_argument(self.safety_question.full_name,
                                 action=argparse.BooleanOptionalAction,
                                 help=self.safety_question.help_message,
                                 default=argparse.SUPPRESS)

        args_parser.add_argument(self.shutdown.full_name,
                                 action=argparse.BooleanOptionalAction,
                                 help=self.shutdown.help_message,
                                 default=argparse.SUPPRESS)

        args_parser.add_argument(self.path.abbreviation_name, self.path.full_name,
                                 type=str,
                                 help=self.path.help_message,
                                 default=argparse.SUPPRESS)

        args_parser.add_argument(self.quality.abbreviation_name, self.quality.full_name,
                                 type=int,
                                 help=self.quality.help_message,
                                 default=argparse.SUPPRESS)

        args_parser.add_argument(self.folder.abbreviation_name, self.folder.full_name,
                                 type=str,
                                 help=self.folder.help_message,
                                 default=argparse.SUPPRESS)

        args_parser.add_argument(self.higher.abbreviation_name, self.higher.full_name,
                                 type=int,
                                 help=self.higher.help_message,
                                 default=argparse.SUPPRESS)

        args_parser.add_argument(self.below.abbreviation_name, self.below.full_name,
                                 type=int,
                                 help=self.below.help_message,
                                 default=argparse.SUPPRESS)

        args_parser.add_argument(self.extensions.abbreviation_name, self.extensions.full_name,
                                 nargs='*',
                                 help=self.extensions.help_message,
                                 default=argparse.SUPPRESS)

        args_parser.add_argument(self.run.abbreviation_name, self.run.full_name,
                                 action='store_true',
                                 help=self.run.help_message,
                                 default=argparse.SUPPRESS)

    def process_arguments(self, settings):
        self.process_extensions(settings[0].user_arguments)
        self.validate_path(settings[0].user_arguments)
        self.validate_folder_name(settings[0].user_arguments)

    def validate_folder_name(self, user_args):
        if self.folder.name not in user_args:
            return

        if user_args.folder == 'def':
            user_args.folder = self.folder.default

    def process_extensions(self, user_args):
        if self.extensions.name not in user_args:
            return

        for extension in user_args.extensions:
            if not extension.startswith('.'):
                user_args.extensions[user_args.extensions.index(extension)] = '.' + extension

    def validate_path(self, user_args):
        if self.path.name in user_args:
            argument_path = Directory(user_args.path)
            if not argument_path.exists():
                throw(user_args.path + ' path does not exist.')
