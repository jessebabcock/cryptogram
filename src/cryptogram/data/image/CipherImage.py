"""Class for src.cryptogram.data.image.Image

Class used for storing Image data with Pillow
https://pillow.readthedocs.io/en/stable/index.html

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from typing import List, Optional
from multiprocessing import sharedctypes


class CipherImage():

    @staticmethod
    def caesar_image(image, shift):
        image_array = image.load()
        for x in range(image.width):
            for y in range(image.height):
                new_color = ((image_array[x, y][0] + shift) % 255,
                             (image_array[x, y][1] + shift) % 255,
                             (image_array[x, y][2] + shift) % 255,
                             (image_array[x, y][3] + shift) % 255) 
                image_array[x, y] = new_color
