from PyQt5 import QtWidgets
from .charter_UI import Ui_charter
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QAbstractItemView
from PyQt5.QtCore import QModelIndex
from .listModel import listAbstractModel

class charter_ctrl(QtWidgets.QMainWindow):
    def __init__(self):
        super(charter_ctrl, self).__init__()
        self.charter_ui = Ui_charter()
        self.charter_ui.setupUi(self)
        self.model = listAbstractModel()
        self.charter_controller()

    def charter_controller(self):

        # pass

        self.charter_ui.chart_listView.setModel(self.model)
        self.charter_ui.chart_listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.charter_ui.chart_listView.clicked[QModelIndex].connect(self.choosed_chart)

    def choosed_chart(self, index):
        chart = self.model.itemFromIndex(index).data()
        print(chart)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = charter_ctrl()
    window.show()
    sys.exit(app.exec_())