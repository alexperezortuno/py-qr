import qrcode

from PIL import Image, ImageDraw

from url.core import utils

ABSOLUTE_PATH: str = utils.get_absolute_parent_path(__file__)
QR_OUTPUT: str = ''
QR_VERSION: int = 1
QR_BOX_SIZE: int = 10
QR_BORDER: int = 4
IMAGE_TITLE: str = ''
ADD_LOGO: bool = False
QR_FILL_COLOR: str = ''
QR_BACKGROUND_COLOR: str = ''
QR_URL: str = ''


def generate_qr() -> None:
    global QR_OUTPUT
    global QR_VERSION
    global QR_BOX_SIZE
    global QR_BORDER
    global ABSOLUTE_PATH
    global QR_FILL_COLOR
    global QR_BACKGROUND_COLOR
    global QR_URL

    qr = qrcode.QRCode(version=QR_VERSION,
                       box_size=QR_BOX_SIZE,
                       border=QR_BORDER,
                       error_correction=qrcode.constants.ERROR_CORRECT_H)
    output: str = f'{ABSOLUTE_PATH}/../output/{utils.remove_special_chars(utils.remove_extension(QR_OUTPUT))}.png'
    # Define the data to be encoded in the QR code
    data = QR_URL

    # Add the data to the QR code object
    qr.add_data(data)

    # Make the QR code
    qr.make(fit=True)

    # Create an image from the QR code with a black fill color and white background
    img = qr.make_image(fill_color=QR_FILL_COLOR,
                        back_color=QR_BACKGROUND_COLOR)

    # Save the QR code image
    img.save(output)
