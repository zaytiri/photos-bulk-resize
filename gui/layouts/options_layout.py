import textwrap

import PySimpleGUI as sg


def get_options_layout():

    ic_text_value = '"pip install phulize". Any console information regarding installing the CLI will be displayed in the "RUN" tab.'
    wrapper = textwrap.TextWrapper(width=90)
    install_help_text = wrapper.fill(text=ic_text_value)

    cli_options = [
        [sg.Button('Install CLI', tooltip='It will install this program\'s CLI if not installed already.')],
        [sg.Text(install_help_text)],
        [sg.Button('Open configurations folder', key='configs_folder')],
        [sg.Text('', key='error_folder')],
    ]

    return [
        [sg.Frame('CLI Advanced Options', layout=cli_options, font='Any 8', title_color='white', expand_x=True, expand_y=True)]
    ]
