import numpy as np

import cv2
img = cv2.imread(filename='xia/0001_01_ck23100_laplace_fft.png', flags=0)
height, width = img.shape
mask = np.zeros(shape=img.shape)
for i in range(height):
    for j in range(width):
        if img[i,j]==0:
            mask[i,j] =255
cv2.imshow('asf',img)
cv2.imshow('mask',mask)
cv2.imwrite(filename='masks/mask.png', img=mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
