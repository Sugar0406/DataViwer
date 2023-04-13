# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dataReader.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_data_reader(object):
    def setupUi(self, data_reader):
        data_reader.setObjectName("data_reader")
        data_reader.resize(909, 518)
        self.centralwidget = QtWidgets.QWidget(data_reader)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_horizontalLayout = QtWidgets.QHBoxLayout()
        self.table_horizontalLayout.setObjectName("table_horizontalLayout")
        self.data_tableView = QtWidgets.QTableView(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.data_tableView.setFont(font)
        self.data_tableView.setMouseTracking(False)
        self.data_tableView.setObjectName("data_tableView")
        self.table_horizontalLayout.addWidget(self.data_tableView)
        self.chooseChart_pushButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.chooseChart_pushButton.setFont(font)
        self.chooseChart_pushButton.setObjectName("chooseChart_pushButton")
        self.table_horizontalLayout.addWidget(self.chooseChart_pushButton)
        self.table_horizontalLayout.setStretch(0, 8)
        self.table_horizontalLayout.setStretch(1, 1)
        self.verticalLayout.addLayout(self.table_horizontalLayout)
        self.error_TextLabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.error_TextLabel.sizePolicy().hasHeightForWidth())
        self.error_TextLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.error_TextLabel.setFont(font)
        self.error_TextLabel.setText("")
        self.error_TextLabel.setObjectName("error_TextLabel")
        self.verticalLayout.addWidget(self.error_TextLabel)
        self.choosefile_horizontalLayout = QtWidgets.QHBoxLayout()
        self.choosefile_horizontalLayout.setObjectName("choosefile_horizontalLayout")
        self.filepath_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filepath_lineEdit.sizePolicy().hasHeightForWidth())
        self.filepath_lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.filepath_lineEdit.setFont(font)
        self.filepath_lineEdit.setObjectName("filepath_lineEdit")
        self.choosefile_horizontalLayout.addWidget(self.filepath_lineEdit)
        self.open_importer_Button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.open_importer_Button.setFont(font)
        self.open_importer_Button.setMouseTracking(False)
        self.open_importer_Button.setObjectName("open_importer_Button")
        self.choosefile_horizontalLayout.addWidget(self.open_importer_Button)
        self.verticalLayout.addLayout(self.choosefile_horizontalLayout)
        self.verticalLayout.setStretch(0, 10)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        data_reader.setCentralWidget(self.centralwidget)

        self.retranslateUi(data_reader)
        QtCore.QMetaObject.connectSlotsByName(data_reader)

    def retranslateUi(self, data_reader):
        _translate = QtCore.QCoreApplication.translate
        data_reader.setWindowTitle(_translate("data_reader", "選取資料"))
        self.chooseChart_pushButton.setText(_translate("data_reader", "選擇圖表"))
        self.open_importer_Button.setText(_translate("data_reader", "匯入資料"))

