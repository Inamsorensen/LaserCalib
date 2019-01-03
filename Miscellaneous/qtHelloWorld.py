#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets as qtwidgets

def window():
    app = qtwidgets.QApplication(sys.argv)
    window = qtwidgets.QWidget()
    box = qtwidgets.QLabel(window)

    box.setText('Hello World!')
    window.setGeometry(100, 100, 200, 50)
    box.move(50, 20)
    window.setWindowTitle('PyQt')
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
