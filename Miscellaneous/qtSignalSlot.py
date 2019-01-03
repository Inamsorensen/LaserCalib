#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets as qtwidgets
from PyQt5 import QtCore as qtcore

class window(qtwidgets.QDialog):
    trigger = qtcore.pyqtSignal()
    
    def __init__(self):
        super(window, self).__init__()
        self.init_ui()

    def init_ui(self):     
        button = qtwidgets.QPushButton(self)
        button.setText('Button')
        button.move(50, 20)
        button.clicked.connect(self.button_clicked)

        self.setGeometry(100, 100, 200, 100)
        self.setWindowTitle('Signals and Slots')
        self.show()

    def button_clicked(self):
        print('Button clicked')


if __name__ == '__main__':
    app = qtwidgets.QApplication(sys.argv)
    win = window()
    sys.exit(app.exec_())

