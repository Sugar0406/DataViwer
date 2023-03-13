from PyQt5 import QtWidgets
from Welcome_page_UI import Ui_MainWindow as welcome_page_UI

from .CSVimporter.CSVimporter_ctrl import CSVimporter_MainWindow
from .CSVimporter.CSVimporter_UI import Ui_importer as CSVimporter_UIMainWindow





class Welcome_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(Welcome_MainWindow, self).__init__()
        self.welcome_page_UI = welcome_page_UI()
        self.welcome_page_UI.setupUi(self)


# class CSVimpoter_MainWindow(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(CSVimpoter_MainWindow, self).__init__()
#         self.CSVimpoter_UI = CSVimpoter_UI()
#         self.CSVimpoter_UI.setupUi(self)
        


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcome_window = Welcome_MainWindow()
    CSVimpoter_window = CSVimporter_MainWindow()
    welcome_window.show()

    welcome_window.welcome_page_UI.start_button.clicked.connect(lambda:{welcome_window.close(), CSVimpoter_window.show()})
    sys.exit(app.exec_())