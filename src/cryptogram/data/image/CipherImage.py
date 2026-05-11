"""Class for src.cryptogram.data.image.Image

Class used for storing Image data with Pillow
https://pillow.readthedocs.io/en/stable/index.html

Image algorithms will be based xoring with a seed based
on the phrase given, based on
https://www.nature.com/articles/s41598-025-27142-2

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from typing import List, Optional
from multiprocessing import sharedctypes
from PIL import Image, ImageTk
import numpy as np
import time



class CipherImage():

    @staticmethod
    def flip_image(image, shift: int):
        image_array = np.array(image, dtype=np.uint8)
        rand = np.random.default_rng(seed=shift)
        random_array = rand.integers(0, 256, (image.height, image.width, 4), dtype=np.uint8)
        image_array ^= random_array
        return Image.fromarray(image_array)
