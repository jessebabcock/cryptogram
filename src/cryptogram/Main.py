"""Main Class.

Author: Russell Feldhausen russfeld@ksu.edu
Version: 0.1
"""

from typing import List
from src.cryptogram.gui.MainWindow import MainWindow


class Main:
    """Main Class."""

    @staticmethod
    def main(args: List[str]) -> None:
        """Main method."""
        MainWindow().mainloop()
