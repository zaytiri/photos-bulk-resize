import PySimpleGUI as sg


def get_help_layout():
    urls = {
        'Github': 'https://github.com/zaytiri/photos-bulk-resize',
        'CLI': 'https://pypi.org/project/phulize/',
        'CHANGELOG.md': 'https://github.com/zaytiri/photos-bulk-resize/blob/main/CHANGELOG.md',
        'README.md': 'https://github.com/zaytiri/photos-bulk-resize/blob/main/README.md'
    }

    font = ('Courier New', 11, 'underline')
    return [[sg.Text(txt, tooltip=urls[txt], enable_events=True, font=font, key=f'URL {urls[txt]}')] for txt in urls]