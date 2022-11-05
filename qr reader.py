#!/usr/bin/env python
# coding: utf-8

# Install pre-requisites
#       pip install opencv-python

# Reading QR code from file
import cv2
from pyzbar.pyzbar import decode

img = cv2.imread('qr-gen.png')
data = decode(img)
print(data)
for info in decode(img):
    print(info.data.decode('utf-8'))
    print(info.type)


# Reading QR code from camera
cam = cv2.VideoCapture(0)
cam.set(3,640) # Width
cam.set(4,480) # Height

camera = True
while camera == True:
    success,frame = cam.read()
    for info in decode(frame):
        print(info.data.decode('utf-8'))
        print(info.type)

    cv2.imshow('Testing QR scan',frame)
    cv2.waitKey(1)
##################################################################
'''
# to prevent camera from scanning the same code multiple times
import time

cam = cv2.VideoCapture(0)
cam.set(3,640) # Width
cam.set(4,480) # Height

camera = True

used_scans = []

while camera == True:
    success,frame = cam.read()
    for info in decode(frame):
        if info.data.decode('utf-8') not in used_scans:
            print('\n New code found, scanning...')
            print(info.data.decode('utf-8'))
            print(info.type)
            used_scans.append(info.data.decode('utf-8'))
            print('Camera sleeping for 3 seconds')
            time.sleep(3)
        elif info.data.decode('utf-8') in used_scans:
            print('\n Old code found, scanning...')
            print(info.data.decode('utf-8'))
            print(info.type)
            print('Camera sleeping for 3 seconds')
            time.sleep(3)
    cv2.imshow('Testing QR scan',frame)
    cv2.waitKey(1)
cam.release()
cv2.DestroyAllWindows()
'''
