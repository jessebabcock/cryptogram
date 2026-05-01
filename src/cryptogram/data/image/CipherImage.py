"""Class for src.cryptogram.data.image.Image

Class used for storing Image data with Pillow
https://pillow.readthedocs.io/en/stable/index.html

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from typing import List, Optional
from multiprocessing import sharedctypes


class CipherImage():

    pixel_array = None
    width = None
    height = None

    @staticmethod
    def update_array(width, height):
        CipherImage.pixel_array = sharedctypes.RawArray('i', width * height * 4)
        CipherImage.width = width
        CipherImage.height = height

    @staticmethod
    def run(image, start, end, shift):
        """Thread method."""
        for i in range(start, end, 4):
            CipherImage.pixel_array[i] = image[i][0] + shift
            CipherImage.pixel_array[i+1] = image[i][1] + shift
            CipherImage.pixel_array[i+2] = image[i][2] + shift
            CipherImage.pixel_array[i+3] = image[i][3] + shift

    @staticmethod
    def encrypted_image():
        new_image_array = CipherImage.pixel_array
        new_image_array = [tuple(new_image_array[i:i+4]) for i in range(0, len(new_image_array), 4)]
        new_image = Image.new("RGBA", (CipherImage.width, CipherImage.height))
        new_image.putdata(new_image_array)
        return new_image

