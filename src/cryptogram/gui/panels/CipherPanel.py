"""Class for src.cryptogram.gui.CypherPanel.

This will be a gui for Menu

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

import tkinter as tk
from typing import Mapping, Dict, Union
# mypy: ignore-errors


class CipherPanel(tk.Frame):
    """Gui class for Cyphers."""

    def __init__(self, master: tk.Widget) -> None:
        """Initializes Menu GUI.

        Args:
            master: MainWindow we use to keep
            main window in context

        Returns:
            None
        """
        self.__master: tk.Widget = master
        self.columns = 5
        self.font = self.__master.font
        tk.Frame.__init__(self, master=self.__master)
        for i in range(self.columns):
            self.grid_columnconfigure(i, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.__cipher_label = tk.Label(master=self, text="Ciphers", font=self.font)
        self.__cipher_label.grid(row=0, column=0, padx=10, sticky="WE", columnspan=self.columns)

        caesar_button: tk.Button = tk.Button(master=self, text="Caesar",
                                             command=lambda:
                                             self.action_performed("caesar"))
        caesar_button.grid(**self._grid_dict(1, 0, "NSEW"))
    
        self.__keyphrase_label = tk.Label(master=self, text="Key/Phrase:", font=self.font)
        self.__keyphrase_label.grid(**self._grid_dict(2, 0, "EW"))

        self.keyphrase = tk.Entry(master=self, font=self.font)
        self.keyphrase.grid(**self._grid_dict(2, 2, "NSEW"), columnspan=self.columns - 1)

    def action_performed(self, text: str) -> None:
        """Actions when a button is pressed.

        Args:
            text: String the box has
            that was clicked

        Returns:
            None
        """
        if text == "caesar":
            self.__master.image_panel.cipher.decode(self.__master.image_panel)
            self.__master.update_phrase_text()

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