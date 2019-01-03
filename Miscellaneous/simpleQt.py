#!/usr/bin/env python

import sys
from PyQt5 import QtWidgets as qtwidgets


if __name__ == '__main__':
    app = qtwidgets.QApplication(sys.argv)
    window = qtwidgets.QWidget()
    window.resize(250, 150)
    window.move(300, 300)
    window.setWindowTitle('First Qt Window')
    window.show()
    sys.exit(app.exec_())
