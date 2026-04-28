"""Class for src.gamegrub.gui.PrimaryWindow.

This will be the main window of the program

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

import tkinter as tk
from src.cryptogram.gui.panels.ImagePanel import ImagePanel
from src.cryptogram.gui.panels.CypherPanel import CypherPanel
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

        self.grid_rowconfigure(0, weight=20)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        for i in range(self.columns):
            self.grid_columnconfigure(i, weight=1)

        self.__main = None
        self.load_image_panel()

        self.__cypher_bar = CypherPanel(self)
        self.__cypher_bar.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW", columnspan=self.columns)

        self.__keyphrase_label = tk.Label(master=self, text="Key/Phrase:", font=self.font)
        self.__keyphrase_label.grid(row=2, column=0, padx=10, sticky="WE")

        self._keyphrase = tk.Entry(master=self, font=self.font)
        self._keyphrase.grid(row=2, column=1, padx=10, sticky="WE", columnspan=self.columns - 1)

        cancel_button: tk.Button = tk.Button(master=self, text="Cancel",
                                             command=lambda:
                                             self.action_performed("cancel"),
                                             font=self.font)
        cancel_button.grid(**self._grid_dict(3, 0, "NWSE"), columnspan=self.columns // 2)

        save_button: tk.Button = tk.Button(master=self, text="Save",
                                           command=lambda:
                                           self.action_performed("save"),
                                           font=self.font)
        save_button.grid(**self._grid_dict(3, self.columns // 2, "NSWE"), columnspan=self.columns // 2)

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
