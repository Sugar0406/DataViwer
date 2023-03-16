# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Welcome_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Welcome_page(object):
    def setupUi(self, Welcome_page):
        Welcome_page.setObjectName("Welcome_page")
        Welcome_page.resize(700, 541)
        self.centralwidget = QtWidgets.QWidget(Welcome_page)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.welcome_bar_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(48)
        self.welcome_bar_label.setFont(font)
        self.welcome_bar_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.welcome_bar_label.setAlignment(QtCore.Qt.AlignCenter)
        self.welcome_bar_label.setObjectName("welcome_bar_label")
        self.verticalLayout.addWidget(self.welcome_bar_label)
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.verticalLayout.addWidget(self.start_button)
        Welcome_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(Welcome_page)
        QtCore.QMetaObject.connectSlotsByName(Welcome_page)

    def retranslateUi(self, Welcome_page):
        _translate = QtCore.QCoreApplication.translate
        Welcome_page.setWindowTitle(_translate("Welcome_page", "Welcome"))
        self.welcome_bar_label.setText(_translate("Welcome_page", "WelCome"))
        self.start_button.setText(_translate("Welcome_page", "let\'s Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Welcome_page = QtWidgets.QMainWindow()
    ui = Ui_Welcome_page()
    ui.setupUi(Welcome_page)
    Welcome_page.show()
    sys.exit(app.exec_())

