"""Class for src.cryptogram.gui.CipherPanel.

This will be a panel for cipher selection

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

import tkinter as tk
from typing import Mapping, Dict, Union
# mypy: ignore-errors


class CipherPanel(tk.Frame):
    """Gui class for Cipher selection."""

    def __init__(self, master: tk.Widget) -> None:
        """Initializes Cipher selection Panel.

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
        self.cipher_style = "Caesar"
        self.__current_cipher = None
        self.__shift_amount_label = None

        self.create_caesar_shift()

        self.caesar_button: tk.Button = tk.Button(
            master=self, text="Caesar",
            command=lambda:
            self.action_performed("caesar"),
            relief="sunken")

        self.caesar_button.grid(**self._grid_dict(1, 0, "NSEW"))
        self.caesar_button.bind('<Button>', 'break')
        self.__current_cipher = self.caesar_button

        self.rot_button: tk.Button = tk.Button(master=self, text="Rot13",
                                                command=lambda:
                                                self.action_performed("rot13"))
        self.rot_button.grid(**self._grid_dict(1, 1, "NSEW"))

        self.diagnal_button: tk.Button = tk.Button(master=self, text="Diagnal",
                                                command=lambda:
                                                self.action_performed("diagnal"))
        self.diagnal_button.grid(**self._grid_dict(1, 2, "NSEW"))

        self.__keyphrase_label = tk.Label(master=self,
                                          text="Key/Phrase:",
                                          font=self.font)
        self.__keyphrase_label.grid(**self._grid_dict(2, 0, "EW"))

        self.keyphrase = tk.Entry(master=self, font=self.font)
        self.keyphrase.grid(**self._grid_dict(2, 2, "NSEW"),
                            columnspan=self.columns - 1)

    def action_performed(self, text: str) -> None:
        """Actions when a button is pressed.

        Args:
            text: String the box has
            that was clicked

        Returns:
            None
        """
        if text == "caesar":
            self.create_caesar_shift()
            self.cipher_style = "Caesar"
            self.__current_cipher.unbind('<Button>')
            self.__current_cipher.config(relief="raised")
            self.caesar_button.bind('<Button>', 'break')
            self.caesar_button.config(relief="sunken")
            self.__current_cipher = self.caesar_button
        elif text == "rot13":
            self.destroy_caesar_shift()
            self.cipher_style = "Rot13"
            self.__current_cipher.unbind('<Button>')
            self.__current_cipher.config(relief="raised")
            self.rot_button.bind('<Button>', 'break')
            self.rot_button.config(relief="sunken")
            self.__current_cipher = self.rot_button
        elif text == "diagnal":
            self.destroy_caesar_shift()
            self.cipher_style = "Diagnal"
            self.__current_cipher.unbind('<Button>')
            self.__current_cipher.config(relief="raised")
            self.diagnal_button.bind('<Button>', 'break')
            self.diagnal_button.config(relief="sunken")
            self.__current_cipher = self.diagnal_button
        self.__master.check_cipher_change()
        self.__master.update_phrase_textbox()

    def create_caesar_shift(self) -> None:
        """Helper function for creating shift box for caesar cipher.

        Args:
            None

        Returns:
            None
        """
        if self.__shift_amount_label is not None:
            self.destroy_caesar_shift()
        self.__shift_amount_label = tk.Label(master=self,
                                             text="Shift: ",
                                             font=self.font)
        self.__shift_amount_label.grid(row=0, column=0, padx=10, sticky="W")
        self.shift_scroll = tk.IntVar(value=0)
        self.shift_scroll.trace('w', self.update_shift_amount)
        self.shift_amount_spinbox = tk.Spinbox(self, from_=0, to=126,
                                               textvariable=self.shift_scroll,
                                               justify=tk.RIGHT,
                                               state='readonly')
        self.shift_amount_spinbox.grid(**self._grid_dict(0, 0, "E"))

    def destroy_caesar_shift(self) -> None:
        """Helper function for destroying shift box.

        Args:
            None

        Returns:
            None
        """
        self.__shift_amount_label.destroy()
        self.shift_amount_spinbox.destroy()

    def update_shift_amount(self, *args) -> None:
        """Updates shift amount for caesar cipher.

        Args:
            None

        Returns:
            None
        """
        self.__master.image_panel.cipher.shift_amount = self.shift_scroll.get()
        self.__master.update_phrase_textbox()

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
