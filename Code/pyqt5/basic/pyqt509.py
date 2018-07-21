#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
QComboBox
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QLabel, QComboBox

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        # 创建组件
        self.lbl = QLabel("Ubuntu", self)

        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.activated[str].connect(self.onActivied)
        # 布局
        combo.move(50, 50)
        self.lbl.move(50, 150)

        # 系统设置
        self.resize(300, 200)
        self.center()
        self.setWindowTitle('Buttons')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onActivied(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())