"""Class for src.cryptogram.gui.ImagePanel.

This will be a gui for Menu

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

from tkinter.ttk import Scrollbar
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from typing import Mapping, Dict, Union
from src.cryptogram.data.Cipher import Cipher
from src.cryptogram.data.CipherFactory import CipherFactory
import re
from io import BytesIO
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
        self.__image_display = tk.Label(master=self, text="Placeholder", borderwidth=3, relief="solid")
        self.__image_display.grid(**self._grid_dict(0, 0, "NSEW"))
        self.cipher: Cipher = CipherFactory.encrypt("Caesar", "", Image.new("RGBA", (1, 1), (255, 0, 0)))

    def action_performed(self, text: str) -> None:
        """Actions when a button is pressed.

        Args:
            text: String the box has
            that was clicked

        Returns:
            None
        """
        print(text)

    def display_image(self, image):
        self.__image = image
        self.__image_display.config(image=image)
        self.__image_display.image = image
    
    def get_image(self):
        return ImageTk.getimage(self.__image)

    def load_file(self):
        file_name = filedialog.askopenfilename(title='Open a file', initialdir='/home/codio/workspace/python/src/resources')
        name = ""
        if re.match('^.*\.cryptogram$', file_name):
            with open(file_name, "rb") as file:
                binary = file.read()
                name = binary[0:8].replace(b"0", b"")
                height = int.from_bytes(binary[8:12], 'little')
                width = int.from_bytes(binary[12:16], 'little')
                image_shift = int.from_bytes(binary[16:20], 'little')
                phrase_ending = int.from_bytes(binary[20:24], 'little')
                header_point = 24 + phrase_ending
                phrase = binary[24:header_point].replace(b"0", b"")
                new_image = Image.frombytes('RGBA', (width, height), binary[header_point:])
                self.cipher = CipherFactory.encrypt(name.decode(), phrase.decode(), new_image)
                if name == "Caesar":
                    self.cipher.shift_amount = image_shift
                self.cipher.encoded = True
                self.cipher.decode()
        else:
            new_image = Image.open(file_name)
            # # default to caesar with no phrase
            # if self.cipher is not None:
            #     self.cipher.image = new_image
            # else:
            self.cipher = CipherFactory.encrypt(self.__master.cipher_bar.cipher_style, "", new_image)
        self.__master.update_encoded_text()
        self.__master.current_key.set(self.cipher.phrase)
        if name != "":
            self.__master.cipher_bar.action_performed(name.decode().lower())
            self.__master.cipher_bar.shift_amount_final.set(self.cipher.shift_amount)
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