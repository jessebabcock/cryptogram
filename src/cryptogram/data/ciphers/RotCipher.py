"""Class for src.cryptogram.data.ciphers.RotCipher.

Rot13 cipher that works the same as Caesar but shift
is 13

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from PIL import Image
from src.cryptogram.data.Cipher import Cipher
from src.cryptogram.data.image.CipherImage import CipherImage
from typing import List
# mypy: ignore-errors


class RotCipher(Cipher):
    """Rot13's Cipher encryption."""

    _instance = None

    def __init__(self, phrase: str, image: Image) -> None:  # type: ignore
        """Initialization.

        Args:
            phrase: phrase to store
            image: image to store
        """
        self.__name: str = "Rot13"
        self.__shift_amount: int = 13
        self.__phrase: str = phrase
        self.__image: Image = image
        self.__encoded: bool = False
        self._seed_pad: int = (42 * 8191) + self.__shift_amount

    def __new__(cls, phrase: str, image: Image) -> "RotCipher":
        """Returns singleton instance for Rot13 Cipher.

        Args:
            None

        Returns:
            RotCipher: Singleton instance
            of RotCipher.
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
            value: phrase to set
        """
        self.__phrase = value

    @property
    def shift_amount(self) -> str:
        """shift_amount getter.

        Args:
            None

        Returns:
            int: Shift amount
        """
        return self.__shift_amount

    @shift_amount.setter
    def shift_amount(self, value: int) -> None:
        """shift_amount setter, does nothing.

        Args:
            value: shift amount to set
        """
        return

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
            value: encoded bool to set
        """
        self.__encoded = value

    @property
    def image(self) -> Image:
        """Image getter.

        Args:
            None

        Returns:
            Image: Current state of the image
        """
        return self.__image

    @image.setter
    def image(self, value: Image) -> None:
        """Image setter.

        Args:
            value: image to set
        """
        self.__image = value

    def encode(self, phrase: str) -> None:
        """Method for encoding.

        Args:
            phrase: new phrase to encode
        """
        if self.encoded:
            self.decode()
        self.encoded = True
        image_shift = 0
        encoded_phrase: List[str] = list()
        for char in phrase:
            new_char = ord(char) + self.__shift_amount
            image_shift += new_char * self._seed_pad
            if new_char > ord('~'):
                new_char = ord('!') + (new_char % ord('~')) - 1
                # new_char = new_char - ord('~') + ord('!') - 1
            char = chr(new_char)
            encoded_phrase.append(char)
        self.phrase = "".join(encoded_phrase)
        self.image = CipherImage.flip_image(self.image, image_shift)

    def decode(self) -> None:
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
                # new_char = ord('~') + new_char - ord('!') + 1
                new_char = ord('~') - (abs(ord('!') - new_char) % ord('~')) + 1
            char = chr(new_char)
            image_shift += (new_char + self.__shift_amount) * self._seed_pad
            decoded_phrase.append(char)
        self.phrase = "".join(decoded_phrase)
        self.image = CipherImage.flip_image(self.image, image_shift)

    def save(self, name: str) -> None:
        """Method for saving to binary.

        8 bytes for name
        4 bytes for width
        4 bytes for height
        4 bytes for shift amount
        4 bytes for length of phrase
        rest of header is the phrase
        ----------------------------
        image data in bytes

        Args:
            name: Filename
        """
        if not self.encoded:
            self.encode(self.phrase)
        phrase_padding: int = len(self.phrase)
        file_content: List[bytes] = [
            self.name.encode().zfill(8),
            self.image.height.to_bytes(4, 'little'),
            self.image.width.to_bytes(4, 'little'),
            self.__shift_amount.to_bytes(4, 'little'),
            phrase_padding.to_bytes(4, 'little'),
            self.phrase.encode()]
        file_content.append(self.image.tobytes())
        with open(f"src/resources/{name}.cryptogram", "wb") as file:
            file.write(b"".join(file_content))
