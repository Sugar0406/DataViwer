# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\CSVimporter.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CSVimporter(object):
    def setupUi(self, CSVimporter):
        CSVimporter.setObjectName("CSVimporter")
        CSVimporter.resize(600, 135)
        self.centralwidget = QtWidgets.QWidget(CSVimporter)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.file_path_textedit = QtWidgets.QTextEdit(self.splitter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.file_path_textedit.setFont(font)
        self.file_path_textedit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.file_path_textedit.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.Taiwan))
        self.file_path_textedit.setObjectName("file_path_textedit")
        self.choose_file_button = QtWidgets.QPushButton(self.splitter)
        self.choose_file_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_file_button.setObjectName("choose_file_button")
        self.verticalLayout.addWidget(self.splitter)
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        self.errorLabel.setFont(font)
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout.addWidget(self.errorLabel)
        CSVimporter.setCentralWidget(self.centralwidget)

        self.retranslateUi(CSVimporter)
        QtCore.QMetaObject.connectSlotsByName(CSVimporter)

    def retranslateUi(self, CSVimporter):
        _translate = QtCore.QCoreApplication.translate
        CSVimporter.setWindowTitle(_translate("CSVimporter", "choose file"))
        self.choose_file_button.setText(_translate("CSVimporter", "打開檔案總管"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CSVimporter = QtWidgets.QMainWindow()
    ui = Ui_CSVimporter()
    ui.setupUi(CSVimporter)
    CSVimporter.show()
    sys.exit(app.exec_())

