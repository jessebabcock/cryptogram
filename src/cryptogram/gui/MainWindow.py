"""Class for src.gamegrub.gui.PrimaryWindow.

This will be the main window of the program

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

import tkinter as tk
from PIL import Image, ImageTk
from src.cryptogram.gui.panels.ImagePanel import ImagePanel
from src.cryptogram.gui.panels.CipherPanel import CipherPanel
from src.cryptogram.data.CipherFactory import CipherFactory
from typing import Mapping, Dict, Union
# mypy: ignore-errors


class MainWindow(tk.Tk):
    """Main window class."""

    def __init__(self) -> None:
        """Initializes Menu GUI.

        Args:
            None

        Returns:
            None
        """
        tk.Tk.__init__(self)
        self.minsize(width=1024, height=740)
        self.title("Cryptogram")
        self.columns = 4
        self.font = ("Arial", 15)

        self.grid_rowconfigure(0, weight=10)
        self.grid_rowconfigure(1, weight=5)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        for i in range(self.columns):
            self.grid_columnconfigure(i, weight=1)

        self.image_panel: tk.Widget = ImagePanel(self)
        self.image_panel.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW", columnspan=self.columns)

        self.cipher_bar = CipherPanel(self)
        self.cipher_bar.grid(row=3, column=0, padx=10, pady=10, sticky="NSEW", columnspan=self.columns)

        encode_button: tk.Button = tk.Button(master=self, text="Encode",
                                              command=lambda:
                                              self.action_performed("encode"),
                                              font=self.font)
        encode_button.grid(**self._grid_dict(1, 2, "NW"))

        decode_button: tk.Button = tk.Button(master=self, text="Decode",
                                              command=lambda:
                                              self.action_performed("decode"),
                                              font=self.font)
        decode_button.grid(**self._grid_dict(1, 1, "NE"))

        self.__current_encryption_phrase = tk.Label(master=self, text="Current key: ", font=self.font)
        self.__current_encryption_phrase.grid(row=0, column=0, padx=10, sticky="NW", columnspan=self.columns)

        load_button: tk.Button = tk.Button(master=self, text="Load Image",
                                             command=lambda:
                                             self.action_performed("load"),
                                             font=self.font)
        load_button.grid(**self._grid_dict(4, 0, "NEWS"), columnspan=2)

        save_button: tk.Button = tk.Button(master=self, text="Save Image",
                                           command=lambda:
                                           self.action_performed("save"),
                                           font=self.font)
        save_button.grid(**self._grid_dict(4, 2, "NWES"), columnspan=2)

    def action_performed(self, text: str) -> None:
        """Actions when a button is pressed.

        Args:
            text: String the box has
            that was clicked

        Returns:
            None
        """
        if text == "load":
            self.image_panel.load_file()
        elif text == "save":
            self.image_panel.cipher.save()
        elif text == "encode":
            phrase = self.cipher_bar.keyphrase.get()
            if self.image_panel.cipher is None or self.image_panel.cipher.name != self.cipher_bar.cipher_style:
                self.image_panel.cipher = CipherFactory.encrypt(self.cipher_bar.cipher_style, phrase, self.image_panel.get_image())
            self.image_panel.cipher.encode(self.image_panel, phrase)
            self.update_phrase_text()
        elif text == "decode":
            self.image_panel.cipher.decode(self.image_panel)
            self.update_phrase_text()
        else:
            raise ValueError("Something bad happened in MainWindow")
    
    def update_phrase_text(self):
        self.__current_encryption_phrase.config(text=f"Current key: {self.image_panel.cipher.phrase}")

    def load_image_panel(self) -> None:
        """Loads the main menu panel.

        Args:
            None

        Returns:
            None
        """
        self.load_panel(ImagePanel(self), self.columns)

    def load_panel(self, panel: tk.Widget, columnspan: int) -> None:
        """Loads panel that button was clicked on.

        Args:
            panel: Panel to be loaded to the main
            window

        Returns:
            None
        """
        if self.__main is not None:
            self.__main.destroy()
        self.__main: tk.Widget = panel
        self.__main.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW", columnspan=columnspan)

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
        settings["padx"] = 10
        settings["pady"] = 10
        settings["sticky"] = sticky
        return settings
