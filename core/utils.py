import os
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import SolidFillColorMask, RadialGradiantColorMask, SquareGradiantColorMask, \
    HorizontalGradiantColorMask
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, GappedSquareModuleDrawer, CircleModuleDrawer, \
    VerticalBarsDrawer, HorizontalBarsDrawer


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

def create_dir_if_not_exists(dir_path: str):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def get_img_by_style(qr, style: str, params: dict) -> tuple | None:
    if style.lower() == 'default':
        return qr.make_image(fill_color=params['fill_color'],
                            back_color=params['back_color'])
    if style.lower() == 'rounded':
        return qr.make_image(fill_color=params['fill_color'],
                            back_color=params['back_color'],
                            image_factory=StyledPilImage,
                            module_drawer=RoundedModuleDrawer())
    if style.lower() == 'gapped':
        return qr.make_image(fill_color=params['fill_color'],
                            back_color=params['back_color'],
                            image_factory=StyledPilImage,
                            module_drawer=GappedSquareModuleDrawer())
    if style.lower() == 'circle':
        return qr.make_image(fill_color=params['fill_color'],
                            back_color=params['back_color'],
                            image_factory=StyledPilImage,
                            module_drawer=CircleModuleDrawer())
    if style.lower() == 'hbar':
        return qr.make_image(fill_color=params['fill_color'],
                            back_color=params['back_color'],
                            image_factory=StyledPilImage,
                            module_drawer=HorizontalBarsDrawer())
    if style.lower() == 'vbar':
        return qr.make_image(fill_color=params['fill_color'],
                            back_color=params['back_color'],
                            image_factory=StyledPilImage,
                            module_drawer=VerticalBarsDrawer())
    if style.lower() == 'solid':
        return qr.make_image(fill_color=params['fill_color'],
                            back_color=params['back_color'],
                            image_factory=StyledPilImage,
                            module_drawer=SolidFillColorMask())
    if style.lower() == 'rgradient':
        return qr.make_image(image_factory=StyledPilImage,
                            color_mask=RadialGradiantColorMask(
                                back_color=params['back_color'],
                                center_color=params['center_color'],
                                edge_color=params['edge_color'],
                            ))
    if style.lower() == 'sgradient':
        return  qr.make_image(image_factory=StyledPilImage,
                            color_mask=SquareGradiantColorMask(
                                back_color=params['back_color'],
                                center_color=params['center_color'],
                                edge_color=params['edge_color'],
                            ))
    if style.lower() == 'hgradient':
        return qr.make_image(image_factory=StyledPilImage,
                            color_mask=HorizontalGradiantColorMask(
                                back_color=params['back_color'],
                                left_color=params['left_color'],
                                right_color=params['right_color'],
                            ))

    return None