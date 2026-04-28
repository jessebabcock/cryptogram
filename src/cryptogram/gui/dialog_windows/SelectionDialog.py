"""Dialog class.

Caller for dialog boxes
Heavily modified version of
https://github.com/python/cpython/blob/3.14/Lib/tkinter/simpledialog.py

Majority of attributes found in:
    https://www.tcl-lang.org/man/tcl8.4/TkCmd/wm.htm
    https://tkdocs.com/pyref/toplevel.html

Author: Jesse Babcock jesseb98@ksu.edu
Version: 0.1
"""

import tkinter as tk
from typing import List, Optional
# mypy: ignore-errors


class SelectionDialog(tk.Toplevel):
    """Class for dialog box making."""

    def __init__(self, master: tk.Widget, title: str = "Selection",
                 message: str = "Select an option",
                 options: List[str] = ["Yes", "No", "Cancel"],
                 icon: str = None) -> None:
        """Initializes dialog box creation.

        Args:
            master: Parent window
            title: Title of dialog box
            message: Message to show
            options: Selection options

        Returns:
            None
        """
        if title == " ":
            tk.Toplevel.__init__(self, master, borderwidth=1, relief="solid")
            self.overrideredirect(True)
        else:
            tk.Toplevel.__init__(self, master)
            self.title(title)
        offscreen_width = master.winfo_width() + 1
        offscreen_height = master.winfo_height() + 1
        self.geometry(f"0x0+{offscreen_width}+{offscreen_height}")
        self.__message = message
        self.__options = options
        self.result: Optional[str] = None
        self.__master = master
        self.__icon = None
        if icon:
            self.__icon = tk.PhotoImage(file=f"resources/{icon}.png")
            # resize image
            self.__icon = self.__icon.subsample(20, 20)

        body = tk.Frame(self)
        self.initial_focus = self.body(body)
        body.pack(padx=50 // len(options), pady=15 // len(options))

        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self._place_window()
        self.wait_window(self)

    def body(self, master) -> None:
        """Main creation of dialog box with buttons.

        Args:
            master: Parent window

        Returns:
            None
        """
        if self.__icon:
            message = tk.Label(master=master,
                               text=f" {self.__message}",
                               image=self.__icon,
                               compound=tk.LEFT)
        else:
            message = tk.Label(master=master, text=self.__message)
        message.grid(row=0, column=0, columnspan=len(self.__options),
                     padx=2, pady=2, sticky="EW")
        i: int = 0
        for option in self.__options:
            button = tk.Button(master=master, text=option,
                               command=lambda x=option:  # type: ignore
                               self.action_performed(x))
            button.grid(row=1, column=i, padx=2, pady=2, sticky="EW")
            i += 1

    def buttonbox(self) -> None:
        """Needed for overriding.

        Args:
            None

        Returns:
            None
        """
        pass

    def _place_window(self) -> None:
        """Centering of box is off, bandaid fix.

        Args:
            None

        Returns:
            None
        """
        self.update_idletasks()
        minwidth = self.winfo_reqwidth()
        minheight = self.winfo_reqheight()
        height = self.__master.winfo_height() / 2
        width = self.__master.winfo_width() / 2
        height_offset = int(height) - (minheight // 2)
        width_offset = int(width) - (minwidth // 2)
        self.geometry(f"{minwidth}x{minheight}+{width_offset}+{height_offset}")

    def cancel(self) -> None:
        """Helper function for WM_DELETE_WINDOW.

        Args:
            None

        Returns:
            None
        """
        self.action_performed("Cancel")

    def action_performed(self, text: str) -> None:
        """Actions when a button is pressed.

        Args:
            text: String the box has
            that was clicked

        Returns:
            None
        """
        self.result = text
        self.destroy()
