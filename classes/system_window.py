from PySide2.QtWidgets import QWidget, QAction, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSlider
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os

class SystemWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.main_layout = QVBoxLayout(self)

        self.first_row_layout = QHBoxLayout(self)

        self.start_button = QPushButton(self)
        self.start_button.setText("START")
        self.first_row_layout.addWidget(self.start_button)

        self.rpm_label = QLabel("0000 RPM",self)
        self.first_row_layout.addWidget(self.rpm_label)

        self.gear_label = QLabel("Gear: N", self)
        self.first_row_layout.addWidget(self.gear_label)

        self.speed_label = QLabel("000 Km/h", self)
        self.first_row_layout.addWidget(self.speed_label)

        self.stop_button = QPushButton(self)
        self.stop_button.setText("STOP")
        self.first_row_layout.addWidget(self.stop_button)

        self.second_row_layout = QHBoxLayout(self)

        self.throttle_label = QLabel("Throttle:", self)
        self.second_row_layout.addWidget(self.throttle_label)

        self.throttle_slider = QSlider(Qt.Horizontal)
        self.throttle_slider.setMaximum(100)
        self.throttle_slider.setMinimum(0)
        self.second_row_layout.addWidget(self.throttle_slider)

        self.status_label = QLabel("Status: OFF", self)
        self.second_row_layout.addWidget(self.status_label)

        self.main_layout.addLayout(self.first_row_layout)
        self.main_layout.addLayout(self.second_row_layout)

        self.start_button.clicked.connect(self.ispisi)

    def ispisi(self):
        speed = str(self.throttle_slider.value()) + " Km/h"
        self.speed_label.setText(speed)
        self.rpm_label.setText("1000 RPM")