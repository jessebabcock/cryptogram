"""Class for src.gamegrub.gui.PrimaryWindow.

This will be the main window of the program

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

import tkinter as tk
from src.cryptogram.gui.ImagePanel import ImagePanel
from src.cryptogram.gui.CypherPanel import CypherPanel
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
        self.title("Game Grubs")

        self.grid_rowconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=2)
        self.grid_columnconfigure(0, weight=1)

        self.__main = None
        self.load_image_panel()

        self.__cypher_bar = CypherPanel(self)
        self.__cypher_bar.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

    def load_image_panel(self) -> None:
        """Loads the main menu panel.

        Args:
            None

        Returns:
            None
        """
        self.load_panel(ImagePanel(self))

    def load_panel(self, panel: tk.Widget) -> None:
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
        self.__main.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
