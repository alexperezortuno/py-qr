import qrcode

from PIL import Image, ImageDraw

from url.core import utils

ABSOLUTE_PATH: str = utils.get_absolute_parent_path(__file__)
AUTHENTICATION_TYPES: tuple = ('WPA', 'WPA2', 'WEP', 'NOPASS')
QR_OUTPUT: str = ''
QR_VERSION: int = 1
QR_BOX_SIZE: int = 10
QR_BORDER: int = 4
IMAGE_TITLE: str = ''
ADD_LOGO: bool = False
IMAGE_LOGO: str = f'{ABSOLUTE_PATH}/../assets/wifi-100.png'


def wifi_code(ssid, hidden, authentication_type, password=None) -> str:
    if authentication_type not in AUTHENTICATION_TYPES:
        raise ValueError(f'Invalid authentication type: {authentication_type}')

    if authentication_type.upper() == 'NOPASS':
        return f'WIFI:T:{authentication_type};S:{ssid};H:{hidden};'

    return f'WIFI:T:{authentication_type};S:{ssid};P:{password};H:{hidden};'


def get_new_size(main_im: Image, foot_im: Image) -> tuple[int, int] | list[int]:
    return main_im.size[0], main_im.size[1] + foot_im.size[1]


def get_middle_size(value: int) -> int:
    res: float = value / 2
    return int(res)


def add_logo(output: str) -> None:
    global IMAGE_LOGO
    global ABSOLUTE_PATH

    main_im = Image.open(f'{ABSOLUTE_PATH}/../output/{output}').convert('RGBA')
    foot_im = Image.open(IMAGE_LOGO)
    create_im = Image.new('RGBA',
                          get_new_size(main_im, foot_im),
                          "WHITE")

    copied_im = main_im.copy()
    create_im.paste(copied_im, (0, 0))
    foot_im.resize((get_middle_size(foot_im.size[0]), get_middle_size(foot_im.size[1])))
    create_im.paste(foot_im,
                    (get_middle_size(main_im.size[0]) - get_middle_size(foot_im.size[0]), create_im.size[1] - foot_im.size[1] - 15),
                    mask=foot_im)
    create_im.save(f'{ABSOLUTE_PATH}/../output/{output}', 'PNG')

    # # Definir las coordenadas del área donde se va a agregar la imagen al pie
    # x, y = main_im.size[0] - foot_im.size[0], main_im.size[1] - foot_im.size[1]
    #
    # # Dibujar la imagen al pie de la imagen principal
    # draw.bitmap((x, y), foot_im, fill=None)
    #
    # # Guardar la nueva imagen con el pie agregado
    # main_im.save(output)


def generate_qr(ssid: str, hidden: bool, authentication_type: str, password: str) -> None:
    global QR_OUTPUT
    global QR_VERSION
    global QR_BOX_SIZE
    global QR_BORDER
    global IMAGE_TITLE
    global ABSOLUTE_PATH

    code = wifi_code(ssid, hidden, authentication_type, password)
    QR_OUTPUT = utils.remove_special_chars(utils.remove_extension(QR_OUTPUT)) + '.png'
    qr = qrcode.QRCode(
        version=QR_VERSION,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=QR_BOX_SIZE,
        border=QR_BORDER,
    )
    qr.add_data(code)
    qr.print_ascii()
    qr.make_image().save(f'{ABSOLUTE_PATH}/../output/{QR_OUTPUT}')

    if ADD_LOGO:
        add_logo(QR_OUTPUT)
