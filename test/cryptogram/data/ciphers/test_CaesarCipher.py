"""Test Class for src.cryptogram.data.cipher.CaesarCipher.

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from src.cryptogram.data.ciphers.CaesarCipher import CaesarCipher
from src.cryptogram.data.Cipher import Cipher
from PIL import Image


class TestCaesarCipher:
    """Test Class for CaesarCipher."""

    def test_caesar_initialization(self) -> None:
        """Test initialization."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        cipher = CaesarCipher("test", image, 42)
        assert cipher.name == "Caesar"
        assert cipher.image == image
        assert cipher.phrase == "test"
        assert cipher.encoded is False
        assert cipher.shift_amount == 42
        assert cipher._seed_pad == (42 * 8191) + cipher.shift_amount

    def test_caesar_is_cipher(self) -> None:
        """Test interface."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        cipher = CaesarCipher("test", image, 42)
        assert isinstance(cipher, Cipher)

    def test_caesar_singleton(self) -> None:
        """Test singleton."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        cipher = CaesarCipher("test", image, 42)
        ciphertwo = CaesarCipher("new", image, 2)
        assert cipher is ciphertwo

    def test_caesar_encode(self) -> None:
        """Test encode on general word."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "test"
        cipher = CaesarCipher(old_phrase, image, 1)
        cipher.encode(old_phrase)
        for i, char in enumerate(cipher.phrase):
            assert ((ord(char) - ord(old_phrase[i])) == 1)

    def test_caesar_encode_wrapping(self) -> None:
        """Test encode on wrapping letter."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "~"
        cipher = CaesarCipher(old_phrase, image, 1)
        cipher.encode(old_phrase)
        assert (cipher.phrase == "!")

    def test_caesar_reencoding(self) -> None:
        """Test encode on already encoded cipher."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "~"
        cipher = CaesarCipher(old_phrase, image, 1)
        cipher.encoded = True
        cipher.encode(old_phrase)
        assert (cipher.phrase == "!")

    def test_caesar_decode(self) -> None:
        """Test decode on general word."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "test"
        cipher = CaesarCipher(old_phrase, image, 1)
        cipher.encoded = True
        cipher.decode()
        for i, char in enumerate(cipher.phrase):
            assert ((ord(char) - ord(old_phrase[i])) == -1)

    def test_caesar_decode_wrapping(self) -> None:
        """Test decode on wrapping letter."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "!"
        cipher = CaesarCipher(old_phrase, image, 1)
        cipher.encoded = True
        cipher.decode()
        assert (cipher.phrase == "~")

    def test_caesar_decode_blocked(self) -> None:
        """Test decode on non-encoded cipher."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "!"
        cipher = CaesarCipher(old_phrase, image, 1)
        cipher.decode()
        assert (cipher.phrase == "!")
