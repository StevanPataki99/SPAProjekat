from PySide2.QtWidgets import QWidget, QAction, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSlider
from PySide2.QtCore import *
from PySide2.QtGui import *
import sys
import os
import threading
import time

class SystemWindow(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.status = False

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
        self.throttle_slider.setMaximum(70)
        self.throttle_slider.setMinimum(-30)
        self.second_row_layout.addWidget(self.throttle_slider)

        self.status_label = QLabel("Status: OFF", self)
        self.second_row_layout.addWidget(self.status_label)

        self.main_layout.addLayout(self.first_row_layout)
        self.main_layout.addLayout(self.second_row_layout)

        self.start_button.clicked.connect(self.thread_init)

        self.stop_button.clicked.connect(self.process_stop)
        self.stop_button.setDisabled(True)

    def thread_init(self):

        self.status = True
        x = threading.Thread(target=self.process_loop)
        x.start()

    def process_loop(self):

        self.system_start() 
        speed = 0
        rpm = 800
        gear = [1, 2, 3, 4, 5, 6]
        current_gear = gear[0]
        while self.status == True:
            time.sleep(0.1)

            self.gear_label.setText("Gear: {}".format(current_gear))

            thrrottle = self.throttle_slider.value()
            if thrrottle >= 0:
                thrrottle += 1
                rpm += thrrottle * 1.45
            elif thrrottle < 0:
                rpm += thrrottle * 1.45
            
            if current_gear == 6:
                if rpm > 6010:
                    rpm = 6000
            elif current_gear == 1:
                if rpm < 745:
                    rpm = 750
            
            if rpm > 4100 and current_gear != 6:
                current_gear = gear[current_gear]
                rpm = 1800
            elif rpm < 1500 and current_gear != 1:
                current_gear = gear[current_gear - 2]
                rpm = 2600

            if thrrottle > 0 and rpm < 6000:
                print((- (current_gear - 7)))
                speed += ((- (current_gear - 7)) * (rpm * 0.00015))
            elif thrrottle < 0:
                speed -=  0.5
            
            if speed < 0:
                speed = 0
            if speed > 260:
                 speed = 260

            self.rpm_label.setText(str(int(rpm)) + " RPM")
            self.speed_label.setText(str(int(speed)) + " Km/h")

        self.system_reset()
        
    def system_start(self):
        self.stop_button.setDisabled(False)
        self.start_button.setDisabled(True)

        self.status_label.setText("Status: ON")

        self.rpm_label.setText("800 RPM")
        self.speed_label.setText("0 Km/h")

    def process_stop(self):

        self.status = False
        
    def system_reset(self):

        self.speed_label.setText("000 Km/h")
        self.rpm_label.setText("0000 RPM")
        self.gear_label.setText("Gear: N")
        self.status_label.setText("Status: OFF")

        self.stop_button.setDisabled(True)
        self.start_button.setDisabled(False)
        