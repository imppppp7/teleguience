import cv2
import numpy as np
from copy import deepcopy

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
n = 0
list1 = []
# mouse callback function


def draw_circle(event,x,y,flags,param):
    global drawing, mode, n, list1
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        list1.append((x, y))
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                list1.append((x, y))
                # cv2.circle(img, (x, y), 4, (0, 255, 0), -1)
                # cv2.circle(img2, (x, y), 3, (255, 255, 255), -1)
                cv2.line(img, list1[n], list1[n+1], (0, 255, 0), thickness=5)
                cv2.line(img2, list1[n], list1[n + 1], (0, 255, 0), thickness=5)
                n = n + 1
            else:
                img[y - 25:y + 25, x - 25:x + 25, :] = img_copy[y - 25:y + 25, x - 25:x + 25, :]
                img2[y - 25:y + 25, x - 25:x + 25, :] = img2_copy[y - 25:y + 25, x - 25:x + 25, :]

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        list1 = []
        n = 0

img = cv2.imread(r'D:\teleguience\teleguidence\time\piuture\mode.png')
print(img.shape)
img_copy = deepcopy(img)
img2 = np.zeros((1024,1920,3), np.uint8)
img2_copy = deepcopy(img2)
# cv2.namedWindow('image_cp',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image_cp',640,480)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image',640,480)
cv2.namedWindow('image2',cv2.WINDOW_NORMAL)
cv2.resizeWindow('image2',640,480)
# cv2.namedWindow('image2_cp',cv2.WINDOW_NORMAL)
# cv2.resizeWindow('image2_cp',640,480)
cv2.setMouseCallback('image',draw_circle)


while(1):
    cv2.imshow('image',img)
    # cv2.imshow('image_cp',img_copy)
    cv2.imshow('image2',img2)
    # cv2.imshow('image2_cp', img2)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == ord('q'):
        break
cv2.destroyAllWindows()