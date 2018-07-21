#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
事件发送
sender()方法的方式决定了事件源
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QDesktopWidget, QGridLayout, QPushButton

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        # 创建组件
        btn1 = QPushButton("Button 1", self)
        btn1.move(30, 50)
        btn2 = QPushButton("Button 2", self)
        btn2.move(150, 50)


        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        # 系统设置
        self.resize(250, 150)
        self.center()
        self.setWindowTitle('Signal and slot')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())