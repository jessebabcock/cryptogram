"""Interface for src.cryptogram.data.ciphers.

This will be an interface for the Ciphers

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from abc import ABC, abstractmethod
from typing import List, Any


class Cipher(ABC):
    """Interface for ciphers."""

    @classmethod
    def __subclasshook__(cls: object, subclass: type) -> bool | Any:
        """Checks the implementation of callables.

        Args:
            cls: Object to be checked
            subclass: Type of the object being checked

        Return:
            bool or Any: Either returns bool or NotImplemented (Any type)
        """
        if cls is Cipher:
            attrs: List[str] = ['name', 'previous_cipher', 'next_cipher', 'encode', 'decode']
            ret: bool = True
            for attr in attrs:
                ret = (ret and
                       hasattr(subclass, attr))
            return ret
        return NotImplemented

    @property
    @abstractmethod
    def name(self) -> str:
        """Abstract method for name getter.

        Args:
            None
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def previous_cipher(self):
        """Abstract method for previous Cipher getter.

        Args:
            None
        """
        raise NotImplementedError

    @property
    @abstractmethod
    def next_cipher(self):
        """Abstract method for next Cipher getter.

        Args:
            None
        """
        raise NotImplementedError
    
    @property
    @abstractmethod
    def phrase(self) -> str:
        """Abstract method for phrase getter.

        Args:
            None
        """
        raise NotImplementedError

    @abstractmethod
    def encode(self, image, phrase) -> None:
        """Abstract method for encoding.

        Args:
            None
        """
        raise NotImplementedError

    @abstractmethod
    def decode(self, image, phrase) -> None:
        """Abstract method for decoding.

        Args:
            None
        """
        raise NotImplementedError