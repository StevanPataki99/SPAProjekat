from PySide2.QtWidgets import QApplication, QFrame
import sys
import time

from classes.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(480, 130)
    window.show()

    app.exec_()
    app.exit()