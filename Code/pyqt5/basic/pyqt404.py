#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
选择字体
"""

import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QDesktopWidget, QGridLayout, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        # 创建组件
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)  

        # 系统设置
        self.resize(250, 180)
        self.center()
        self.setWindowTitle('File dialog')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Example()

    sys.exit(app.exec_())