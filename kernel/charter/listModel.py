from PyQt5.QtCore import QAbstractItemModel, QModelIndex

class listAbstractModel(QAbstractItemModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.listItem = [('折線圖', 'plot'), ('散點圖','scatter')]

    def data(self):
        for index in range(0, len(self.listItem)):
            self.setItemData(self.listItem[index][0])



    def rowCount(self, parent=QModelIndex()):
        return len(self.listItem)

    # setting number of column
    def columnCount(self, parent=QModelIndex()):
        return 0
        