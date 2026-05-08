"""Class for src.cryptogram.data.image.Image

Class used for storing Image data with Pillow
https://pillow.readthedocs.io/en/stable/index.html

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from typing import List, Optional
from multiprocessing import sharedctypes
from PIL import Image, ImageTk
import fastrand
#https://github.com/lemire/fastrand/blob/master/README.md


class CipherImage():

    @staticmethod
    def caesar_image(window, image, shift):
        #maybe look into flattened data
        image_array = image.load()
        fastrand.pcg32_seed(shift)
        for x in range(image.width):
            for y in range(image.height):
                # randbits much faster than randint
                new_color = ((image_array[x, y][0] + fastrand.pcg32bounded(255)) % 255,
                             (image_array[x, y][1] + fastrand.pcg32bounded(255)) % 255,
                             (image_array[x, y][2] + fastrand.pcg32bounded(255)) % 255,
                             (image_array[x, y][3] + fastrand.pcg32bounded(255)) % 255) 
                image_array[x, y] = new_color
            if x % 5 == 0:
                window.display_image(ImageTk.PhotoImage(image))
                window.update_idletasks()
            
