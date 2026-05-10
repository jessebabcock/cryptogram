"""Class for src.cryptogram.data.ciphers.Caesar

Caesar cipher that can change shift amount from input

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

import multiprocessing
from PIL import Image, ImageTk
from src.cryptogram.data.Cipher import Cipher
from src.cryptogram.data.image.CipherImage import CipherImage
from typing import List, Optional


class CaesarCipher(Cipher):
    """Caesar's Cipher encryption."""

    _instance = None

    def __init__(self, phrase: str, image, shift_amount: int) -> None:
        self.__name: str = "Ceasar Cipher"
        self.__shift_amount: int = shift_amount
        self.__phrase: str = phrase
        self.__image = image
        self.__encoded = False
        self.__seed_pad = (42 * 8191)

    def __new__(cls, phrase: str, image, shift_amount: int) -> "CustomItemList":
        """Returns singleton instance for custom item list.

        Args:
            None

        Returns:
            CustomItemList: Singleton instance
            of CustomItemList.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @property
    def name(self) -> str:
        """Name getter.

        Args:
            None

        Returns:
            str: Name
        """
        return self.__name

    @property
    def phrase(self) -> str:
        """Phrase getter.

        Args:
            None

        Returns:
            str: Phrase
        """
        return self.__phrase

    @phrase.setter
    def phrase(self, value: str) -> None:
        """Phrase setter.

        Args:
            None
        """
        self.__phrase = value
    
    @property
    def encoded(self) -> bool:
        """Encoded bool getter.

        Args:
            None

        Returns:
            bool: Wether its encoded or not
        """
        return self.__encoded

    @encoded.setter
    def encoded(self, value: bool) -> None:
        """Encoded bool getter.

        Args:
            None
        """
        self.__encoded = value
    
    @property
    def image(self) -> str:
        """Image getter.

        Args:
            None

        Returns:
            str: Current state of the image
        """
        return self.__image

    @image.setter
    def image(self, value: str) -> None:
        """Image setter.

        Args:
            None
        """
        self.__image = value

    def encode(self, window) -> None:
        """Method for encoding.

        Args:
            None
        """
        if self.encoded:
            return
        self.encoded = True
        image_shift = 0
        encoded_phrase: List[str] = list()
        for char in self.phrase:
            new_char = ord(char) + self.__shift_amount
            image_shift += new_char * self.__seed_pad
            if new_char > ord('~'):
                new_char = new_char - ord('~') + ord('!') - 1
            char = chr(new_char)
            encoded_phrase.append(char)
        self.phrase = "".join(encoded_phrase)
        self.__encoded_image = CipherImage.flip_image(window, self.image, image_shift)
        window.display_image(ImageTk.PhotoImage(self.__encoded_image))

    def decode(self, window) -> None:
        """Method for decoding.

        Args:
            None
        """
        if not self.encoded:
            return
        self.encoded = False
        image_shift = 0
        decoded_phrase: List[str] = list()
        for char in self.phrase:
            new_char = ord(char) - self.__shift_amount
            if new_char < ord('!'):
                new_char = ord('~') + new_char - ord('!') + 1
            char = chr(new_char)
            image_shift += (new_char + self.__shift_amount) * self.__seed_pad
            decoded_phrase.append(char)
        self.phrase = "".join(decoded_phrase)
        self.image = CipherImage.flip_image(window, self.__encoded_image, image_shift)
        window.display_image(ImageTk.PhotoImage(self.image))