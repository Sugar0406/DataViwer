# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\charter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_charter(object):
    def setupUi(self, charter):
        charter.setObjectName("charter")
        charter.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(charter)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(100, 100, 611, 391))
        self.tableView.setObjectName("tableView")
        charter.setCentralWidget(self.centralwidget)

        self.retranslateUi(charter)
        QtCore.QMetaObject.connectSlotsByName(charter)

    def retranslateUi(self, charter):
        _translate = QtCore.QCoreApplication.translate
        charter.setWindowTitle(_translate("charter", "選擇圖表"))

