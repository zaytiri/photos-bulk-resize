import PySimpleGUI as sg

from gui.utils import list_configs


def get_run_layout():
    outcome_layout = [
        [
            sg.Button('Open converted photos\' folder', key='conv_folder'),
            sg.Button('Open original photos\' folder', key='ori_folder'),
            sg.Button('Open output summary file', key='outcome_file')
        ]
    ]

    configs = list_configs()
    path = '-> (no folder defined)'

    if len(configs) > 0:
        path = '-> ' + configs['path']

    return [
        [sg.Text('Click "RUN" to resize photos for following folder:')],
        [sg.Text(path, key='show_path')],
        [sg.HorizontalSeparator()],
        [sg.Text('Make sure you have a backup for the folder to be converted BEFORE running the program.')],
        [sg.Multiline("",
                      autoscroll=True,
                      write_only=True,
                      auto_refresh=True,
                      disabled=True,
                      expand_x=True,
                      size=(None, 10),
                      echo_stdout_stderr=True,
                      reroute_stdout=True)
         ],
        [sg.Text('', key='run_error')],
        [sg.Button('RUN')],
        [sg.Frame('Outcome', outcome_layout, font='Any 8', title_color='white', expand_x=True, visible=False, key='outcome_frame')]
    ]
