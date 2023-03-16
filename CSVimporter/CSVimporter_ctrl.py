from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
from .CSVimporter_UI import Ui_CSVimporter



'''
import the data come from filetype '.xlsx' or '.csv'
if not -> show error text in errorLabel

'''

class CSVimporter_ctrl(QtWidgets.QMainWindow):
    def __init__(self):
        super(CSVimporter_ctrl, self).__init__()
        self.CSVimporter_UI = Ui_CSVimporter()
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
            self.CSVimporter_UI.errorLabel.setStyleSheet("color:red")
            self.CSVimporter_UI.errorLabel.setText('錯誤檔案格式,請使用.xlsx或.csv檔案')

        


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = CSVimporter_ctrl()
    window.show()
    sys.exit(app.exec_())