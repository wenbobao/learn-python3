#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
状态栏
1. 调用QtGui.QMainWindow类的statusBar()方法，创建状态栏。
2. showMessage()方法在状态栏上显示一条信息。
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        self.statusBar().showMessage('Ready')
        self.resize(250,150)
        self.center()
        self.setWindowTitle('Center')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())