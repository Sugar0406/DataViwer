from PyQt5 import QtWidgets
from Welcome_page_UI import Ui_Welcome_page as welcome_page_UI
from dataReader.dataReader_ctrl import dataReader_ctrl
# from CSVimporter.CSVimporter_ctrl import CSVimporter_ctrl

class Welcome_ctrl(QtWidgets.QMainWindow):
    def __init__(self):
        super(Welcome_ctrl, self).__init__()
        self.welcome_page_UI = welcome_page_UI()
        self.welcome_page_UI.setupUi(self)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcome_window = Welcome_ctrl()
    dataReader_window = dataReader_ctrl()
    welcome_window.show()

    # juimp to datareader
    welcome_window.welcome_page_UI.start_button.clicked.connect(lambda:{welcome_window.close(), dataReader_window.show()})
    sys.exit(app.exec_())