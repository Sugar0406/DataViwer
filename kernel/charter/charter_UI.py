# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\charter.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_charter(object):
    def setupUi(self, charter):
        charter.setObjectName("charter")
        charter.resize(293, 227)
        self.centralwidget = QtWidgets.QWidget(charter)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(14)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chart_listView = QtWidgets.QListView(self.centralwidget)
        self.chart_listView.setObjectName("chart_listView")
        self.verticalLayout.addWidget(self.chart_listView)
        charter.setCentralWidget(self.centralwidget)

        self.retranslateUi(charter)
        QtCore.QMetaObject.connectSlotsByName(charter)

    def retranslateUi(self, charter):
        _translate = QtCore.QCoreApplication.translate
        charter.setWindowTitle(_translate("charter", "選擇圖表"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    charter = QtWidgets.QMainWindow()
    ui = Ui_charter()
    ui.setupUi(charter)
    charter.show()
    sys.exit(app.exec_())
