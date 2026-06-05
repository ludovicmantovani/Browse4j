"""Main entry point for Browse4j."""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui.designer.MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


def main() -> None:
    """Run the application."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
