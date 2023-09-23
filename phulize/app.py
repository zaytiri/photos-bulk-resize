import subprocess
import sys

from phulize.search import Search
from phulize.settings.manager import Manager
from phulize.utils.log import throw


def main(custom_args=None, is_gui=False):
    arguments = Manager().configure_arguments(custom_args, is_gui)

    validate_settings(arguments['Settings'], is_gui)

    result = run_resizer(arguments['Settings'], is_gui)

    if arguments['Settings'].shutdown.value and not is_gui:
        subprocess.run(["shutdown", "-s"])

    return result


def run_resizer(arguments, is_gui):
    photos = Search(arguments)

    if not arguments.run.value:
        return

    epilogue(arguments)

    if arguments.safety_question.value and not is_gui:
        response = input(
            'Are you sure you want to continue? \n [Y/n]')
        if response == 'n' or response == 'N':
            sys.exit()
        elif response == 'Y':
            photos.search()
            return

    return photos.search()


def validate_settings(arguments, is_gui):
    if not arguments.path.value:
        throw('Path is empty.', to_exit=not is_gui)

    if arguments.shutdown.value and not is_gui:
        print('The computer will be shutdown when this program is done.\n')


def epilogue(arguments):
    print('All images found with the a ', end="")
    first = True
    for extension in arguments.extensions.value:
        if first:
            print(extension, end="")
            first = False
            continue
        print(' or ' + extension, end="")
    print(
        ' extension are going to be resized and be kept in the "' +
        arguments.folder.value + '" folder.')
    print('\n"' + arguments.path.value + '" is going to be modified permanently.\n')


if __name__ == '__main__':
    main()
