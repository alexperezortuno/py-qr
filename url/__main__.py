
#!/usr/bin/env python
import argparse
import getpass
import sys

from url.core import generator

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--output', default='url_qr', help='Output file name')
    parser.add_argument('-q', '--qr-version', default=1, type=int, help='QR code version')
    parser.add_argument('--box-size', default=40, type=int, help='QR code box size')
    parser.add_argument('--border', default=1, type=int, help='QR code border size')
    parser.add_argument('-f', '--fill', default='black', help='Fill color of the QR code')
    parser.add_argument('-b', '--background', default='white', help='Background color of the QR code')
    parser.add_argument('-u', '--url', help='URL to encode in the QR code')

    args = parser.parse_args()

    if not args.url:
        print('Error: URL is required')
        sys.exit(1)

    generator.QR_VERSION = args.qr_version
    generator.QR_BOX_SIZE = args.box_size
    generator.QR_BORDER = args.border
    generator.QR_OUTPUT = args.output
    generator.QR_FILL_COLOR = args.fill
    generator.QR_BACKGROUND_COLOR = args.background
    generator.QR_URL = args.url

    generator.generate_qr()
