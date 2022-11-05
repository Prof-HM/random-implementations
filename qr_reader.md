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
