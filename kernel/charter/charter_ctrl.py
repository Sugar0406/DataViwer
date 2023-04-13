from PyQt5 import QtWidgets
from .charter_UI import Ui_charter

class charter_ctrl(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.charter_ui = Ui_charter
        self.charter_ui.setupUi(self)