"""Class for src.cryptogram.data.image.CipherImage.

Image algorithm will be based xoring
on the phrase given with a premade random field,
based on https://www.nature.com/articles/s41598-025-27142-2

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from PIL import Image
import numpy as np
# mypy: ignore-errors


class CipherImage():
    """Static class for image algo we apply."""

    @staticmethod
    def flip_image(image: Image, shift: int) -> Image:
        """Method for XORing random pixels with image.

        Args:
            image: Image to flip
            shift: shift we apply

        Returns:
            Image: final result of the XOR
        """
        image_array = np.array(image, dtype=np.uint8)
        rand = np.random.default_rng(seed=shift)
        random_array = rand.integers(
            0,
            256,
            (image.height, image.width, 4),
            dtype=np.uint8)
        image_array ^= random_array
        return Image.fromarray(image_array)
