import cv2
import numpy as np

# Create a black background
img = np.zeros((600, 800, 3), np.uint8)

drawing = False
ix, iy = -1, -1

# Mouse callback function
def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
