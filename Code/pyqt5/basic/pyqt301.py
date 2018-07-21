#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Signals & slots
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber,  QSlider, QVBoxLayout, QApplication, QDesktopWidget

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        # 创建组件
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        # 布局
        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
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


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())