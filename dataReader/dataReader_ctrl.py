from PyQt5 import QtWidgets
from .dataReader_UI import Ui_data_reader
from ..CSVimporter.CSVimporter_ctrl import CSVimporter_ctrl


class dataReader_ctrl(QtWidgets.QMainWindow):
    def __init__(self):
        super(dataReader_ctrl, self).__init__()
        self.data_reader_ui = Ui_data_reader()
        self.data_reader_ui.setupUi(self)
        

    def controller(self):
        self.data_reader_ui.open_importer_Button.clicked.connect(self.open_importer())
        self.childWindow = CSVimporter_ctrl()

    def open_importer(self):
        self.childWindow.show()

        



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = dataReader_ctrl()
    window.show()
    sys.exit(app.exec_())