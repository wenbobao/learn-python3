#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
自定义信号发送
sender()方法的方式决定了事件源
"""

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QDesktopWidget


class Communicate(QObject):
    closeApp = pyqtSignal()

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        
        # 系统设置
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Emit signal')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())