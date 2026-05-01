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

    def __init__(self, phrase: str, image, shift_amount: int) -> None:
        self.__name: str = "Ceasar Cipher"
        self.__shift_amount: int = shift_amount
        self.__phrase: str = phrase
        self.__image = image


    @property
    def name(self) -> str:
        """Name getter.

        Args:
            None
        """
        return self.__name

    @property
    def phrase(self) -> str:
        """Phrase getter.

        Args:
            None
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
    def image(self) -> str:
        """Phrase getter.

        Args:
            None
        """
        return self.__image

    @image.setter
    def image(self, value: str) -> None:
        """Phrase setter.

        Args:
            None
        """
        self.__image = value

    def encode(self, window) -> None:
        """Method for encoding.

        Args:
            None
        """
        encoded_phrase: List[str] = list()
        for char in self.phrase:
            new_char = (ord(char) + self.__shift_amount)
            if new_char > ord('~'):
                new_char = ord('!') + (new_char % ord('!'))
            char = chr(new_char)
            encoded_phrase.append(char)
        self.phrase = "".join(encoded_phrase)

        # threads = 2
        # start = 0
        # scale = self.image.width * self.image.height
        # step = scale // threads
        # thread_array = [None] * threads
        # image_array = list(self.image.getdata())
        # for i in range(threads):
        #     if i == 3:
        #         if step * threads > scale:
        #             step -= ((step * (threads - 1)) - scale)
        #     thread_array[i] = multiprocessing.Process(target=CipherImage.run, args=(image_array, start, start + step, self.__shift_amount))
        #     thread_array[i].start()
        #     start += step

        # for i in range(threads):
        #     thread_array[i].join()

        CipherImage.caesar_image(self.image, self.__shift_amount)

    def decode(self) -> None:
        """Method for decoding.

        Args:
            None
        """
        decoded_phrase: List[str] = list()
        for char in self.phrase:
            new_char = (ord(char) - self.__shift_amount)
            if new_char < ord('a'):
                new_char = new_char + ord('z') % ord('a')
            char = chr(new_char)
            decoded_phrase.append(char)
        self.phrase = "".join(decoded_phrase)