#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
制作提交反馈信息的布局

grid.setSpacing(10) -> 创建标签之间的空间

grid.addWidget(reviewEdit, 3, 1, 5, 1) -> 可以指定组件的跨行和跨列的大小。这里我们指定这个元素跨5行显示
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QGridLayout, QApplication, QDesktopWidget

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
    
        # 创建组件
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        # 布局
        gird = QGridLayout()
        gird.setSpacing(10)

        gird.addWidget(title, 1, 0)
        gird.addWidget(titleEdit, 1, 1)

        gird.addWidget(author, 2, 0)
        gird.addWidget(authorEdit, 2, 1)

        gird.addWidget(review, 3, 0)
        gird.addWidget(reviewEdit, 3, 1, 5, 1)

        self.setLayout(gird)

        # 系统设置
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