#!/usr/bin/env python
# coding: utf-8

# # Install pre-requisites
#       pip install pyqrcode
#       pip install pypng

import pyqrcode
import png
from pyqrcode import QRCode


# # Generate one QR code
s = "123456"

url = pyqrcode.create(s)
url.png('qr-gen.png',scale = 6)
print("QR code has been generated")


# # Generate Multiple QR code
s = ["123456","789012"]
counter = 0
for i in s:
    print(counter)
    filename = "qr-gen-" + str(counter) + ".png"
    url = pyqrcode.create(s[counter])
    url.png(filename,scale = 6)
    print(f"QR code {counter} has been generated")
    counter += 1

# # Further exploration
# 1. Generate QR code that contains a whole list
# 2. Generating Dynamic QR Code
