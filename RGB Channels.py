import matplotlib.pyplot as plt
import skimage.io as io
from copy import deepcopy
import cv2
import glob
from pathlib import Path


path = glob.glob("C:/Users/abril/Documents/Modular/Electronic-Polarization-Camera/*.jpg")
cv_img = []

for pic in path:

    image = io.imread(pic)
    r = deepcopy(image)
    g = deepcopy(image)
    b = deepcopy(image)

    r[:,:,1] = 0
    r[:,:,2] = 0

    g[:,:,0] = 0
    g[:,:,2] = 0

    b[:,:,0] = 0
    b[:,:,1] = 0

    fig, ax = plt.subplots(ncols=2, nrows = 2)

    ax[0,0].imshow(image)
    ax[0,0].set_title('Original')

    ax[0,1].imshow(r)
    ax[0,1].set_title('red')

    ax[1,0].imshow(g)
    ax[1,0].set_title('green')

    ax[1,1].imshow(b)
    ax[1,1].set_title('blue')

plt.show()
