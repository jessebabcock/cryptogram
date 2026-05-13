"""Test Class for src.cryptogram.data.cipher.RotCipher.

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from src.cryptogram.data.ciphers.RotCipher import RotCipher
from src.cryptogram.data.Cipher import Cipher
from PIL import Image


class TestCaesarCipher:
    """Test Class for RotCipher."""

    def test_rot_initialization(self) -> None:
        """Test initialization."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        cipher = RotCipher("test", image)
        assert cipher.name == "Rot13"
        assert cipher.image == image
        assert cipher.phrase == "test"
        assert cipher.encoded is False
        assert cipher.shift_amount == 13
        assert cipher._seed_pad == (42 * 8191) + cipher.shift_amount

    def test_rot_singleton(self) -> None:
        """Test singleton."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        cipher = RotCipher("test", image)
        ciphertwo = RotCipher("new", image)
        assert cipher is ciphertwo

    def test_rot_is_cipher(self) -> None:
        """Test interface."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        cipher = RotCipher("test", image)
        assert isinstance(cipher, Cipher)

    def test_rot_encode(self) -> None:
        """Test encode on general word."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "aaaa"
        cipher = RotCipher(old_phrase, image)
        cipher.encode(old_phrase)
        for i, char in enumerate(cipher.phrase):
            assert ((ord(char) - ord(old_phrase[i])) == 13)

    def test_rot_encode_wrapping(self) -> None:
        """Test encode on wrapping letter."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "~"
        cipher = RotCipher(old_phrase, image)
        cipher.encode(old_phrase)
        assert (cipher.phrase == "-")

    def test_rot_reencoding(self) -> None:
        """Test encode on already encoded cipher."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "a"
        cipher = RotCipher(old_phrase, image)
        cipher.encoded = True
        cipher.encode(old_phrase)
        assert (cipher.phrase == "n")

    def test_rot_decode(self) -> None:
        """Test decode on general word."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "nnnn"
        cipher = RotCipher(old_phrase, image)
        cipher.encoded = True
        cipher.decode()
        for i, char in enumerate(cipher.phrase):
            assert ((ord(char) - ord(old_phrase[i])) == -13)

    def test_rot_decode_wrapping(self) -> None:
        """Test decode on wrapping letter."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "-"
        cipher = RotCipher(old_phrase, image)
        cipher.encoded = True
        cipher.decode()
        assert (cipher.phrase == "~")

    def test_rot_decode_blocked(self) -> None:
        """Test decode on non-encoded cipher."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "!"
        cipher = RotCipher(old_phrase, image)
        cipher.decode()
        assert (cipher.phrase == "!")
