from phulize.app import main


def run_resizer():
    return __run(['--run'])


def edit_configs(to_edit):
    args = []
    for key in to_edit.keys():
        args.append('--' + key)
        if to_edit[key][1]:
            for v in to_edit[key][0]:
                args.append(v)
        else:
            args.append(to_edit[key][0])

    __run(args)


def __run(args):
    return main(args, is_gui=True)
