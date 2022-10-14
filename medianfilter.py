import signal
from tkinter import Image

import cv2
import numpy as np

from convolution import imageName

image = cv2.imread('car1.png')
data = []
width, height = image.size
for h in range(height):
    row = []
    for w in range(width):
        value = image.getpixel((w,h))
        row.append(value)
        data.append(row)

    data = np.float32(data)
    data = signal.medfilt2d(data,(3,3))

for h in range(height):
    for w in range(width):
        image.putpixel((w,h), int(data[w][h]))
        image.save('result.png')