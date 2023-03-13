from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from .CSVimporter_UI import Ui_MainWindow


'''
Use to import the data come from filetype '.xlsx' or '.csv'

'''

class CSVimporter_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(CSVimporter_MainWindow, self).__init__()
        self.CSVimporter_UI = Ui_MainWindow()
        self.CSVimporter_UI.setupUi(self)
        self.CSVimpoter_controller()

    # main controler
    def CSVimpoter_controller(self):
        self.CSVimporter_UI.file_path_textedit.setText('選擇資料來源')
        self.CSVimporter_UI.choose_file_button.clicked.connect(self.choose_file)


    # choose file from computer
    def choose_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open file", "./")
        file_type = file_path.split('.')[-1]
        
        if file_type == 'xlsx' or file_type == 'csv':
            self.CSVimporter_UI.file_path_textedit.setText(file_path)
            self.CSVimporter_UI.errorLabel.setText('')
        else:
            self.CSVimporter_UI.file_path_textedit.setText(file_path)
            self.CSVimporter_UI.errorLabel.setText('錯誤檔案格式')


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = CSVimporter_MainWindow()
    window.show()
    sys.exit(app.exec_())