# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
# |--settings
# |--mainapp
# |--adminapp
# |--authapp

import os


def create_main(dir_name):
    try:
        os.mkdir(dir_name)
    except FileExistsError as e:
        print(f'dir exists: {e.filename}')
    return 0


def create_nest_dir(parent, *dirs):
    for el in dirs:
        try:
            dir_path = os.path.join(parent, el)
            os.mkdir(dir_path)
        except FileExistsError as e:
            print(f'dir exists: {e.filename}')
        return 0


def create_sarter(main_dir):
    create_sarter('my_project')


create_nest_dir('settings', 'mainapp', 'adminapp', 'authapp')
