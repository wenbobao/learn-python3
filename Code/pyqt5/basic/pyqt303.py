#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
事件对象
self.setMouseTracking(True) -> 开启鼠标追踪
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QGridLayout, QLabel

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        # 创建组件
        x = 0
        y = 0

        self.text = "x: {0}, y: {1}".format(x, y)
        self.label = QLabel(self.text, self)

        # 布局
        gird = QGridLayout()
        gird.setSpacing(10)

        gird.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(gird)

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

    def mouseMoveEvent(self, e):

        x = e.x()
        y = e.y()

        text = "x: {0}, y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())