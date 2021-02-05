from PyQt5 import QtWidgets
from add_model import *  # импорт нашего сгенерированного файла
import sys
from BD import Orm


class AddPass(QtWidgets.QDialog):
    def __init__(self):
        super(AddPass, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.buttonBox.accepted.connect(self.add)
        self.ui.buttonBox.rejected.connect(self.close)

        self.bd = Orm()

    def add(self):
        name = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        self.bd.addlog(name, password)
        self.close()
