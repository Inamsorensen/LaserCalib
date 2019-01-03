#!/usr/bin/env/ python

import sys, os
from PyQt5 import QtWidgets as qtwidgets
from PyQt5 import QtGui as qtgui

class Example(qtwidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Qt with Icon')

        self.show()

if __name__ == '__main__':
    app = qtwidgets.QApplication(sys.argv)
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'icon_64x64.png')
    print(path)
    example = Example()
    app.setWindowIcon(qtgui.QIcon(path))
    sys.exit(app.exec_())


