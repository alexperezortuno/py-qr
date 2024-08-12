import os


def get_absolute_path(path):
    if path.startswith('/'):
        return path
    return os.path.join(os.path.dirname(__file__), path)


def get_absolute_parent_path(path):
    return os.path.dirname(get_absolute_path(path))


def remove_special_chars(file_name: str) -> str:
    return ''.join(e for e in file_name if e.isalnum() or e in ['-', '_'])


def remove_extension(file_name: str) -> str:
    return file_name.split('.')[0]