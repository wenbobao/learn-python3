#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
选择字体
"""

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QGridLayout, QVBoxLayout, QPushButton, QSizePolicy, QLabel, QFontDialog

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        # 创建组件
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)
        btn.move(30, 20)
        btn.clicked.connect(self.showDialog)
        
        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)
        
        vbox = QVBoxLayout()
        vbox.addWidget(btn)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        # 系统设置
        self.resize(250, 180)
        self.center()
        self.setWindowTitle('Font dialog')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
            self.lbl.setFont(font)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())