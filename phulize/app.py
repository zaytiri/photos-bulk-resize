import subprocess
import sys

from phulize.search import Search
from phulize.settings.manager import Manager
from phulize.utils.log import throw


def main():
    print('program entrypoint')
    arguments = Manager().configure_arguments()

    if not arguments['Settings'].path.value:
        throw('Path is empty.')

    epilogue(arguments['Settings'])

    if arguments['Settings'].shutdown.value:
        print('The computer will be shutdown when this program is done.\n')

    photos = Search(arguments['Settings'])

    if arguments['Settings'].safety_question.value:
        response = input(
            'Are you sure you want to continue? \n [Y/n]')
        if response == 'n' or response == 'N':
            sys.exit()
        elif response == 'Y':
            photos.search()
            return

    photos.search()

    if arguments['Settings'].shutdown.value:
        subprocess.run(["shutdown", "-s"])


def epilogue(arguments):
    print('All photos found with the a ', end="")
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
