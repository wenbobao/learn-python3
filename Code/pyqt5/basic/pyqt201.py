#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
绝对定位
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QDesktopWidget

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    

        lbl1 = QLabel('A', self)
        lbl1.move(15, 10)      

        lbl2 = QLabel('B', self)
        lbl2.move(35, 40) 

        lbl3 = QLabel('C', self)
        lbl3.move(55, 70) 

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