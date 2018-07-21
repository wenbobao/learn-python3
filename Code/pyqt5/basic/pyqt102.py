#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
菜单栏
1. 调用QtGui.QMainWindow类的statusBar()方法，创建状态栏。
2. showMessage()方法在状态栏上显示一条信息。
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget, QAction, qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAct)
        

        self.resize(250,150)
        self.center()
        self.setWindowTitle('Simple menu')
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