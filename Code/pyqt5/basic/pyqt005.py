#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
消息盒子
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Message box')

        self.show()

    # 如果关闭QWidget，就会产生一个QCloseEvent。改变控件的默认行为，就是替换掉默认的事件处理。
    def closeEvent(self, event):
        
        reply = QMessageBox.question(self, "Message", "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())