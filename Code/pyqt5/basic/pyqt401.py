#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
输入文字
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QGridLayout, QInputDialog, QLineEdit, QPushButton

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        # 创建组件
        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)
        # 布局

        # 系统设置
        self.center()
        self.setWindowTitle('Buttons')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())