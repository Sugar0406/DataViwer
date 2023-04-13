from PyQt5.QtCore import Qt, QAbstractTableModel, QModelIndex

class tableAbstractModel(QAbstractTableModel):
    def __init__(self, dataList, dataHeader, parent=None):
        super().__init__(parent)
        self.data_value = dataList
        self.header = dataHeader

    # settting model data
    def data(self, index, role):
        row = index.row()
        column = index.column()
        if role in { Qt.DisplayRole, Qt.EditRole}:
            return self.data_value[row][column]
        
    # setting number of row
    def rowCount(self, parent=QModelIndex()):
        return len(self.data_value)

    # setting number of column
    def columnCount(self, parent=QModelIndex()):
        return len(max(self.data_value, key=len)) if self.rowCount() else 0

    # settimg column header
    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole: # only change what DisplayRole returns
            if orientation == Qt.Horizontal:
                return self.header[section]
        return super().headerData(section, orientation, role) # must have this line

    # let data can edit
    def flags(self, index):
        return super().flags(index) | Qt.ItemIsEditable
    
    def setData(self, index, newValue, role=Qt.EditRole):
        if role in (Qt.DisplayRole, Qt.EditRole):
            
            # if not input any new Value, not change the oringinal Value
            if not newValue:
                return False
            
            self.data_value[index.row()][index.column()] = newValue
            return self.data_value



