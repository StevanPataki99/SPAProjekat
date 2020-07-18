from PySide2.QtWidgets import QMainWindow, QApplication, QAction, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
import sys
import os
from classes.system_window import SystemWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.sys_window = SystemWindow(self)
        self.setCentralWidget(self.sys_window)
        
        
        
