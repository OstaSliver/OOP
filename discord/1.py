import numpy as np
import cv2
from mss import mss
from PIL import Image

bounding_box = {'top': 0, 'left': 0, 'width': 600, 'height': 500}

sct = mss()


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        bounding_box['top'] = y
        bounding_box['left'] = x

while True:
    sct_img = sct.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))

    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break

    if cv2.getWindowProperty('screen', cv2.WND_PROP_VISIBLE) < 1:
        break
    
    # change top left position with mouse position
    if cv2.getWindowProperty('screen', cv2.WND_PROP_VISIBLE) == 1:
        cv2.setMouseCallback('screen', mouse_callback)
        cv2.waitKey(1)



