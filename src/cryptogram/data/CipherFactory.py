"""Class for src.cryptogram.data.CipherFactory.

Factory for ciphers

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from src.cryptogram.data.ciphers.CaesarCipher import CaesarCipher
from src.cryptogram.data.Cipher import Cipher
from src.cryptogram.data.ciphers.RotCipher import RotCipher
from PIL import Image
# mypy: ignore-errors


class CipherFactory():
    """Static class for cipher factory."""

    @staticmethod
    def encrypt(cipher: str, phrase: str, image: Image) -> Cipher:
        """Method for getting and constructing cipher.

        Args:
            cipher: name of cipher
            phrase: phrase with the cipher
            image: image to apply cipher to

        Returns:
            Cipher: construction of cipher
        """
        cipher = cipher.lower()
        if cipher == "caesar":
            shift_amount = 0
            return CaesarCipher(phrase, image, shift_amount)
        elif cipher == "rot13":
            shift_amount = 13
            return RotCipher(phrase, image)
        else:
            raise ValueError("No cipher with that name")
