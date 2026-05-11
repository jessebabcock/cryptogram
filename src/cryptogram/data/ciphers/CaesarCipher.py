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
import re
import struct


class CaesarCipher(Cipher):
    """Caesar's Cipher encryption."""

    _instance = None

    def __init__(self, phrase: str, image, shift_amount: int) -> None:
        self.__name: str = "Caesar"
        self.__shift_amount: int = shift_amount
        self.__phrase: str = phrase
        self.__image = image
        self.__encoded = False
        self.__seed_pad = (42 * 8191) + shift_amount

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

    def encode(self, window, phrase) -> None:
        """Method for encoding.

        Args:
            None
        """
        if self.encoded:
            self.decode(window)
        self.encoded = True
        image_shift = 0
        encoded_phrase: List[str] = list()
        for char in phrase:
            new_char = ord(char) + self.__shift_amount
            image_shift += new_char * self.__seed_pad
            if new_char > ord('~'):
                new_char = new_char - ord('~') + ord('!') - 1
            char = chr(new_char)
            encoded_phrase.append(char)
        self.phrase = "".join(encoded_phrase)
        self.image = CipherImage.flip_image(window, self.image, image_shift)
        window.display_image(ImageTk.PhotoImage(self.image))

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
        self.image = CipherImage.flip_image(window, self.image, image_shift)
        window.display_image(ImageTk.PhotoImage(self.image))

    def save(self) -> str:
        # .encode() is byte format not cipher, bool is 1 byte but helps with padding
        # 42 byte header
        print(self.image.height.to_bytes(4, 'little'))
        file_content = [self.name.encode().zfill(8),
                        self.image.height.to_bytes(4, 'little'),
                        self.image.width.to_bytes(4, 'little'),
                        self.__shift_amount.to_bytes(2, 'little'),
                        self.encoded.to_bytes(1, 'little'),
                        self.phrase.encode().zfill(20),
                        '/'.encode()]
        file_content.append(self.image.tobytes())
        with open("test.cryptogram", "wb") as file:
            file.write(b"".join(file_content))