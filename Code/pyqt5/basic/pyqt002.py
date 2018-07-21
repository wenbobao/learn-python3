#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
带窗口图标
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("Icon")
        self.setWindowIcon(QIcon('web.png'))

        self.show()


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())