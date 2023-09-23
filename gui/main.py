import PySimpleGUI as sg

from gui.api import run_resizer, edit_configs
from gui.cli_options import go_to_settings_files, install_program
from gui.layouts.help_layout import get_help_layout
from gui.layouts.options_layout import get_options_layout
from gui.layouts.run_layout import get_run_layout
from gui.layouts.view_edit_layout import get_view_edit_layout
from gui.utils import check_editable_config, open_file, list_configs, path_exists, get_icon_path


def make_window():
    layout = [
        [sg.TabGroup(
            [
                [
                    sg.Tab('Run', get_run_layout()),
                    sg.Tab('View/Edit', get_view_edit_layout()),
                    sg.Tab('Options', get_options_layout()),
                    sg.Tab('Help', get_help_layout())
                ]
            ])
        ]
    ]
    win = sg.Window('Photo Resizer GUI', layout, finalize=True, icon=get_icon_path())
    return win


window = make_window()

result = {}

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'RUN':
        window['run_error'].update('')
        window['outcome_frame'].update(visible=False)

        if len(list_configs()) == 0:
            window['run_error'].update('ERR: >> No configurations defined.')
            continue

        if not path_exists(values['edit_path']):
            window['run_error'].update('ERR: >> Current defined folder to be converted does not exist.')
            continue

        window['run_error'].update('RUNNING: while running, this windows could be non responsive.')
        result = run_resizer()
        window['run_error'].update('DONE.')
        window['outcome_frame'].update(visible=True)

    if event == 'EDIT':
        window['edit_info'].update('')
        to_edit = {}

        values['edit_quality'] = str(int(values['edit_quality']))

        check_editable_config(values, 'path', 'edit_path', to_edit)
        check_editable_config(values, 'extensions', 'edit_extensions', to_edit, is_list=True)
        check_editable_config(values, 'folder', 'edit_folder', to_edit)
        check_editable_config(values, 'quality', 'edit_quality', to_edit)
        check_editable_config(values, 'below', 'edit_below', to_edit)
        check_editable_config(values, 'higher', 'edit_higher', to_edit)

        edit_configs(to_edit)
        if len(to_edit.keys()) > 0:
            window['edit_info'].update('Saved configurations: ' + ', '.join(to_edit.keys()))
            window['show_path'].update('-> ' + window['edit_path'].get())
        else:
            window['edit_info'].update('Nothing to save.')

    if event == 'ORIGINAL':
        window['edit_folder'].update('_ORIGINAL')

    if event == 'Install CLI':
        install_program()

    if event == 'configs_folder' and not go_to_settings_files():
        window['error_folder'].update('ERROR: The settings folder does not exist yet. Add new Schedules.')

    if event == 'conv_folder' and len(result) != 0:
        open_file(result['path'])
    if event == 'ori_folder' and len(result) != 0:
        open_file(result['folder'])
    if event == 'outcome_file' and len(result) != 0:
        open_file(result['output_file'])

window.close()
