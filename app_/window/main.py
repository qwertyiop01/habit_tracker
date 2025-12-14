#!/bin/python3

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton
from PyQt6.QtWidgets import QMessageBox, QGridLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('your habit master dangen/ window it is ahuennoe')
    
if __name__ == '__main__':
    app=QApplication(sys.argv)
    run = MyApp()
    run.show()
    sys.exit(app.exec())