"""Class for src.cryptogram.gui.ImagePanel.

This will be a gui for Menu

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

import tkinter as tk
from typing import Mapping, Dict, Union
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

        self.__place_holder = tk.Label(master=self, text="Placeholder", borderwidth=3, relief="solid")
        self.__place_holder.grid(**self._grid_dict(0, 0, "NSEW"))

    def action_performed(self, text: str) -> None:
        """Actions when a button is pressed.

        Args:
            text: String the box has
            that was clicked

        Returns:
            None
        """
        print(text)
        
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