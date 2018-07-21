#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
选取颜色
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QGridLayout, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QColor

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        # 创建组件

        color = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 20)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" 
            % color.name())
        self.frm.setGeometry(130, 22, 100, 100) 

        # 系统设置
        self.resize(250, 180)
        self.center()
        self.setWindowTitle('Color dialog')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showDialog(self):
        color = QColorDialog.getColor()

        if color.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }"
                % color.name())


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())