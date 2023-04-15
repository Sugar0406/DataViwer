from PyQt5 import QtWidgets
from .dataReader_UI import Ui_data_reader
from PyQt5.QtWidgets import QFileDialog, QTableWidgetItem

from .tableModel import tableAbstractModel
# from ..charter.charter_ctrl import charter_ctrl
from ..charter.charter_ctrl import charter_ctrl

import pandas as pd


class dataReader_ctrl(QtWidgets.QMainWindow):
    def __init__(self):
        super(dataReader_ctrl, self).__init__()
        self.dataReader_ui = Ui_data_reader()
        self.dataReader_ui.setupUi(self)

        self.model = None
        self.dataReader_conterller()
        

    def dataReader_conterller(self):
        # set importer_button  
        self.dataReader_ui.open_importer_Button.setToolTip("開啟檔案總管並選擇資料檔")

        # set chart_button
        self.dataReader_ui.chooseChart_pushButton.setToolTip("選擇圖表")
        self.dataReader_ui.chooseChart_pushButton.setVisible(False)
        
        #set button event
        self.dataReader_ui.open_importer_Button.clicked.connect(self.import_csv)
        self.dataReader_ui.chooseChart_pushButton.clicked.connect(self.choose_chart)



    def choose_chart(self):
        pass


    # button event for importer_button
    def import_csv(self):   

        # choose file from Windows_Explorer
        file_path, _ = QFileDialog.getOpenFileName(self, "Open file", "./")

        # test choose file is correct file type
        file_type = file_path.split('.')[-1]
        if file_type == 'xlsx' or file_type == 'csv':
            self.dataReader_ui.filepath_lineEdit.setText(file_path)
            self.dataReader_ui.error_TextLabel.setText("")
            self.set_tableWidget(file_path, file_type)
        else:
            self.dataReader_ui.filepath_lineEdit.setText("")
            self.dataReader_ui.error_TextLabel.setStyleSheet("color:red")
            self.dataReader_ui.error_TextLabel.setText('錯誤檔案格式,請使用.xlsx或.csv檔案')


    # set the abstractDataModel to the ViewModel
    def set_tableWidget(self, file_path, file_type):

        # read Data Use DataFrame
        if file_type == 'csv':
            data = pd.read_csv(file_path)
        else:
            data = pd.read_excel(file_path)
        data_header = data.columns.tolist()
        data_value = data.values.tolist()

        # create abstractModel
        self.model = tableAbstractModel(dataList=data_value, dataHeader=data_header)
        # set modelView
        self.dataReader_ui.data_tableView.setModel(self.model)
        self.dataReader_ui.data_tableView.resizeColumnsToContents()

        # show the button to choose chart
        self.dataReader_ui.chooseChart_pushButton.setVisible(True)
        
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = dataReader_ctrl()
    window.show()
    sys.exit(app.exec_())