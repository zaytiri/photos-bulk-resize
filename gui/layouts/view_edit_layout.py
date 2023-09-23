import PySimpleGUI as sg

from gui.utils import list_configs


def get_view_edit_layout():
    configs = list_configs()

    path = ''
    extensions = []
    folder = ''
    quality = 55
    below = 0
    higher = 0

    if len(configs) > 0:
        path = configs['path']
        extensions = configs['extensions']
        folder = configs['folder']
        quality = configs['quality']
        below = configs['below']
        higher = configs['higher']

    view_configs_layout = [
        [sg.Text('View or edit current configurations:')],
        [
            sg.Text('path', tooltip='Path of the folder to be converted.', size=(10, 1)),
            sg.Input(path, key='edit_path', expand_x=True),
            sg.FolderBrowse()
        ],
        [
            sg.Text('extensions', tooltip='A list of extensions, with or without dot(.), separated by spaces.', size=(10, 1)),
            sg.Input(' '.join(extensions), key='edit_extensions', expand_x=True)
        ],
        [
            sg.Text('folder', tooltip='The name of the folder for the original photos to be saved in the same folder hierarchy.', size=(10, 1)),
            sg.Input(folder, key='edit_folder', expand_x=True),
            sg.Button('ORIGINAL')
        ],
        [
            sg.Text('quality',
                    tooltip='The quality to convert all photos, in percentage. Inputting 50 equals a decrease in quality by 50%º, approximately.',
                    size=(10, 1)),
            sg.Slider((0, 100), default_value=quality, orientation='h', expand_x=True, key='edit_quality')],
        [
            sg.Text('below', tooltip='All photos that are below than this value will be converted. If 0, this value will be ignored', size=(10, 1)),
            sg.Input(below, key='edit_below', expand_x=True)
        ],
        [
            sg.Text('higher', tooltip='All photos that are higher than this value will be converted. If 0, this value will be ignored', size=(10, 1)),
            sg.Input(higher, key='edit_higher', expand_x=True)
        ],
        [sg.Text('', key='edit_info')],
        [sg.Button('EDIT')]
    ]

    return view_configs_layout
