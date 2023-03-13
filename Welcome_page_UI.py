# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Welcome_page.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 541)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome_bar_label.setText(_translate("MainWindow", "WelCome"))
        self.start_button.setText(_translate("MainWindow", "let\'s Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

