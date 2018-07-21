#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
简单的窗口
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250,250)
    w.move(300,300)
    w.setWindowTitle('simple')
    w.show()

    sys.exit(app.exec_())