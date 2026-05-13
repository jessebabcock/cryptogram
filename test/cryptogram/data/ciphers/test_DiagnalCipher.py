"""Test Class for src.cryptogram.data.cipher.DiagnalCipher.

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from src.cryptogram.data.ciphers.DiagnalCipher import DiagnalCipher
from src.cryptogram.data.Cipher import Cipher
from PIL import Image


class TestDiagnalCipher:
    """Test Class for DiagnalCipher."""

    def test_diagnal_initialization(self) -> None:
        """Test initialization."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        cipher = DiagnalCipher("test", image)
        assert cipher.name == "Diagnal"
        assert cipher.image == image
        assert cipher.phrase == "test"
        assert cipher.encoded is False
        assert cipher.shift_amount == 0
        assert cipher._seed_pad == (42 * 8191) + cipher.shift_amount

    def test_diagnal_is_cipher(self) -> None:
        """Test interface."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        cipher = DiagnalCipher("test", image)
        assert isinstance(cipher, Cipher)

    def test_diagnal_singleton(self) -> None:
        """Test singleton."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        cipher = DiagnalCipher("test", image)
        ciphertwo = DiagnalCipher("new", image)
        assert cipher is ciphertwo

    def test_diagnal_encode(self) -> None:
        """Test encode on general word."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "test"
        cipher = DiagnalCipher(old_phrase, image)
        cipher.encode(old_phrase)
        for i, char in enumerate(cipher.phrase):
            assert ((ord(char) ^ ord(old_phrase[i])) == 20)

    def test_diagnal_reencoding(self) -> None:
        """Test encode on already encoded cipher."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "a"
        cipher = DiagnalCipher(old_phrase, image)
        cipher.encoded = True
        cipher.encode(old_phrase)
        assert (cipher.phrase == "u")

    def test_diagnal_decode(self) -> None:
        """Test decode on general word."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "u"
        cipher = DiagnalCipher(old_phrase, image)
        cipher.encoded = True
        cipher.decode()
        assert cipher.phrase == "a"

    def test_diagnal_decode_blocked(self) -> None:
        """Test decode on non-encoded cipher."""
        image = Image.new("RGBA", (1, 1), (255, 0, 0))
        old_phrase = "!"
        cipher = DiagnalCipher(old_phrase, image)
        cipher.decode()
        assert (cipher.phrase == "!")
