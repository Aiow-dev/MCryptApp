import os


def create_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)


def create_file(path):
    open(path, 'w+').close()
