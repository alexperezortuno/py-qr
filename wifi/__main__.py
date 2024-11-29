#!/usr/bin/env python
import argparse
import getpass
import sys

from core.constants import AUTHENTICATION_TYPES
from wifi.core import generator

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version',
                        action='store_true',
                        help='Show the version number')
    parser.add_argument('-s', '--ssid',
                        help='SSID of the network',
                        required=True)
    parser.add_argument('--hidden', action='store_false', help='Whether the network is hidden')
    parser.add_argument('-p', '--password', help='Password of the network')
    parser.add_argument('-n', '--nopass', action='store_true', help='Whether the network has no password')
    parser.add_argument('-a', '--authentication-type',
                        choices=AUTHENTICATION_TYPES,
                        default='WPA2',
                        help='Authentication type of the network')
    parser.add_argument('-t', '--title', default="", help='Title of the QR code')
    parser.add_argument('-o', '--output', default='wifi_qr', help='Output file name')
    parser.add_argument('-q', '--qr-version', default=1, type=int, help='QR code version')
    parser.add_argument('-b', '--box-size', default=10, type=int, help='QR code box size')
    parser.add_argument('--border', default=4, type=int, help='QR code border size')
    parser.add_argument('--add-logo', action='store_true', help='Add logo to the QR code')

    args = parser.parse_args()
    password: str = ''
    ssid: str = ''
    authentication_type: str = args.authentication_type
    hidden: bool = args.hidden

    if args.nopass:
        if args.password:
            print('Warning: Password will be ignored')

    if not args.nopass and not args.password:
        password = getpass.getpass()

    if args.password:
        password = args.password

    if args.title:
        generator.IMAGE_TITLE = args.title

    generator.QR_VERSION = args.qr_version
    generator.QR_BOX_SIZE = args.box_size
    generator.QR_BORDER = args.border
    generator.QR_OUTPUT = args.output
    generator.ADD_LOGO = args.add_logo

    if not args.ssid:
        print('SSID is required')
        sys.exit(1)
    else:
        ssid = args.ssid

    generator.generate_qr(ssid, hidden, authentication_type, password)
