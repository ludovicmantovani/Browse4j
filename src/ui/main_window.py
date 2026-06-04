"""Main entry point for Browse4j."""

import sys

from PySide6.QtWidgets import QApplication, QMainWindow


def main() -> None:
    """Run the application."""

    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
