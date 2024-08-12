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


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))
