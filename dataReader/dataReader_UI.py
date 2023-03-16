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
        data_reader.resize(909, 529)
        self.centralwidget = QtWidgets.QWidget(data_reader)
        self.centralwidget.setObjectName("centralwidget")
        self.tets_label = QtWidgets.QLabel(self.centralwidget)
        self.tets_label.setGeometry(QtCore.QRect(190, 240, 401, 81))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.tets_label.setFont(font)
        self.tets_label.setObjectName("tets_label")
        self.open_importer_Button = QtWidgets.QPushButton(self.centralwidget)
        self.open_importer_Button.setGeometry(QtCore.QRect(20, 20, 131, 31))
        self.open_importer_Button.setObjectName("open_importer_Button")
        data_reader.setCentralWidget(self.centralwidget)

        self.retranslateUi(data_reader)
        QtCore.QMetaObject.connectSlotsByName(data_reader)

    def retranslateUi(self, data_reader):
        _translate = QtCore.QCoreApplication.translate
        data_reader.setWindowTitle(_translate("data_reader", "show data"))
        self.tets_label.setText(_translate("data_reader", "TextLabel"))
        self.open_importer_Button.setText(_translate("data_reader", "匯入資料"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    data_reader = QtWidgets.QMainWindow()
    ui = Ui_data_reader()
    ui.setupUi(data_reader)
    data_reader.show()
    sys.exit(app.exec_())

