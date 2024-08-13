#!/usr/bin/env python
import argparse
import getpass
import sys

from core.constants import QR_STYLES
from core.utils import hex_to_rgb
from url.core import generator

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default='url_qr', help='Output file name')
    parser.add_argument('-q', '--qr-version', default=1, type=int, help='QR code version')
    parser.add_argument('--box-size', default=40, type=int, help='QR code box size')
    parser.add_argument('--border', default=1, type=int, help='QR code border size')
    parser.add_argument('-f', '--fill', default='000000', help='Fill color of the QR code')
    parser.add_argument('-b', '--background', default='FFFFFF', help='Background color of the QR code')
    parser.add_argument('-c', '--center-color', default='FFFFFF', help='Center color of the QR code')
    parser.add_argument('-l', '--left-color', default='E0E0E0', help='Left color of the QR code')
    parser.add_argument('-r', '--right-color', default='000000', help='Right color of the QR code')
    parser.add_argument('-e', '--edge-color', default='000000', help='Edge color of the QR code')
    parser.add_argument('-u', '--url', help='URL to encode in the QR code')
    parser.add_argument('-s', '--style',
                        choices=QR_STYLES,
                        default='default', help='QR code style')

    args = parser.parse_args()

    if not args.url:
        print('Error: URL is required')
        sys.exit(1)

    generator.QR_VERSION = args.qr_version
    generator.QR_BOX_SIZE = args.box_size
    generator.QR_BORDER = args.border
    generator.QR_OUTPUT = args.output
    generator.QR_FILL_COLOR = hex_to_rgb(args.fill)
    generator.QR_BACKGROUND_COLOR = hex_to_rgb(args.background)
    generator.QR_URL = args.url
    generator.STYLE = args.style
    generator.LEFT_COLOR = hex_to_rgb(args.left_color)
    generator.RIGHT_COLOR = hex_to_rgb(args.right_color)
    generator.CENTER_COLOR = hex_to_rgb(args.center_color)
    generator.EDGE_COLOR = hex_to_rgb(args.edge_color)

    generator.generate_qr()
