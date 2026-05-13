"""Class for src.cryptogram.gui.ImagePanel.

This will be a gui for Menu

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from typing import Mapping, Dict, Union
from src.cryptogram.data.Cipher import Cipher
from src.cryptogram.data.CipherFactory import CipherFactory
import re
# mypy: ignore-errors


class ImagePanel(tk.Frame):
    """Gui class for the image selection."""

    def __init__(self, master: tk.Widget) -> None:
        """Initializes Menu GUI.

        Args:
            master: MainWindow we use to keep
            main window in context

        Returns:
            None
        """
        self.__master: tk.Widget = master
        tk.Frame.__init__(self, master=self.__master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.__image = None
        self.__image_display = tk.Label(master=self,
                                        text="Placeholder",
                                        borderwidth=3,
                                        relief="solid")
        self.__image_display.grid(**self._grid_dict(0, 0, "NSEW"))
        self.cipher: Cipher = CipherFactory.encrypt(
            "Caesar",
            "",
            Image.new("RGBA", (1, 1), (255, 0, 0)))

    def action_performed(self, text: str) -> None:
        """Actions when a button is pressed.

        Args:
            text: String the box has
            that was clicked

        Returns:
            None
        """
        print(text)

    def display_image(self, image: Image) -> None:
        """Actions when a button is pressed.

        Args:
            image: Image to display

        Returns:
            None
        """
        self.__image = image
        self.__image_display.config(image=image)
        self.__image_display.image = image

    def get_image(self) -> Image:
        """Helper function to get current image.

        Args:
            None

        Returns:
            Image: Current image displayed
        """
        return ImageTk.getimage(self.__image)

    def load_file(self) -> None:
        """Loads file from file explorer.

        Args:
            None

        Returns:
            None
        """
        file_name = filedialog.askopenfilename(
            title='Open a file',
            initialdir='src/resources')
        name = ""
        # somehow \. is deprecated
        file_type = re.escape('.cryptogram')
        if re.match((f'^.*{file_type}$'), file_name):
            with open(file_name, "rb") as file:
                pointer = 0
                binary = file.read()
                name = binary[pointer:pointer + 8].replace(b"0", b"")
                pointer += 8
                height = int.from_bytes(
                    binary[pointer:pointer + 4], 'little')
                pointer += 4
                width = int.from_bytes(
                    binary[pointer:pointer + 4], 'little')
                pointer += 4
                image_shift = int.from_bytes(
                    binary[pointer:pointer + 4], 'little')
                pointer += 4
                phrase_ending = int.from_bytes(
                    binary[pointer:pointer + 4], 'little')
                pointer += 4
                phrase = binary[pointer:pointer + phrase_ending].replace(
                    b"0", b"")
                pointer += phrase_ending
                new_image = Image.frombytes('RGBA',
                                            (width, height),
                                            binary[pointer:])
                self.cipher = CipherFactory.encrypt(name.decode(),
                                                    phrase.decode(),
                                                    new_image)
                if name != "Rot13":
                    self.cipher.shift_amount = image_shift
                self.cipher.encoded = True
                self.cipher.decode()
        else:
            new_image = Image.open(file_name)
            self.cipher = CipherFactory.encrypt(
                self.__master.cipher_bar.cipher_style,
                "",
                new_image)
        self.__master.update_encoded_text()
        self.__master.current_key.set(self.cipher.phrase)
        self.__master.cipher_bar.action_performed(
            self.cipher.name.lower())
        self.__master.cipher_bar.shift_scroll.set(
            self.cipher.shift_amount)
        self.display_image(ImageTk.PhotoImage(self.cipher.image))
        self.__master.decoded_pressed()

    def _grid_dict(self,
                   row: int,
                   column: int,
                   sticky: str) -> Mapping[str, str | int]:
        """Create a dictionary of settings.

        Taken from:
        https://textbooks.cs.ksu.edu/cc410/y-milestones/06-gui-basics/

        Args:
            row: the row for the item
            column: the column for the item
            sticky: the sticky settings
        """
        settings: Dict[str, Union[str, int]] = dict()
        settings["row"] = row
        settings["column"] = column
        settings["padx"] = 2
        settings["pady"] = 2
        settings["sticky"] = sticky
        return settings
