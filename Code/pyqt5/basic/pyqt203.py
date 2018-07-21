#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
栅格布局
QGridLayout

"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QApplication, QDesktopWidget

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        

        gird = QGridLayout()
        self.setLayout(gird)


        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                '4', '5', '6', '*',
                 '1', '2', '3', '-',
                '0', '.', '=', '+']

        positions = [(i,j) for i in range(5) for j in range(4)]


        for position, name in zip(positions, names):
            
            if name == '':
                continue
            
            button = QPushButton(name)

            gird.addWidget(button, *position)

        self.center()
        self.setWindowTitle('Buttons')
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