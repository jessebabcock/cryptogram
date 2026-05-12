"""Class for src.cryptogram.data.CipherFactory.

Factory for ciphers

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from src.cryptogram.data.Cipher import Cipher
from src.cryptogram.data.ciphers.CaesarCipher import CaesarCipher
from src.cryptogram.data.ciphers.RotCipher import RotCipher


class CipherFactory():

    @staticmethod
    def encrypt(cipher: str, phrase: str, image):
        cipher = cipher.lower()
        if cipher == "caesar":
            shift_amount = 0
            return CaesarCipher(phrase, image, shift_amount)
        elif cipher == "rot13":
            shift_amount = 13
            return RotCipher(phrase, image, shift_amount)
            