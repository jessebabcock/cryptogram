"""Class for src.cryptogram.data.ciphers.Caesar

Caesar cipher that can change shift amount from input

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from src.cryptogram.data.Cipher import Cipher
from typing import List, Optional


class CaesarCipher(Cipher):
    """Interface for ciphers."""

    def __init__(self, phrase: str, image, shift_amount: int) -> None:
        self.__name: str = "Ceasar Cipher"
        self.__previous_cipher: Optional[Cipher] = None
        self.__next_cipher: Optional[Cipher] = None
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
    def previous_cipher(self) -> Cipher:
        """Previous Cipher getter.

        Args:
            None
        """
        return self.__previous_cipher

    @property
    def next_cipher(self) -> Cipher:
        """Next Cipher getter.

        Args:
            None
        """
        return self.__next_cipher

    def encode(self) -> None:
        """Method for encoding.

        Args:
            None
        """
        encoded_phrase: List[str] = list()
        for char in self.phrase:
            new_char = (ord(char) + self.__shift_amount)
            if new_char > ord('z'):
                new_char = new_char  % ord('a') + ord('a')
            char = chr(new_char)
            encoded_phrase.append(char)
        self.phrase = "".join(encoded_phrase)

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