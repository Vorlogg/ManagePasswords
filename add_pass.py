from PyQt6 import QtWidgets
from add_model import *  # импорт нашего сгенерированного файла
import sys
from BD import Orm


class AddPass(QtWidgets.QDialog):
    def __init__(self,id=None):
        super(AddPass, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.add)
        self.ui.buttonBox.rejected.connect(self.close)
        self.bd = Orm()
        self.id=id
        if self.id:
            data=self.bd.get_change(self.id)
            self.ui.lineEdit_1.setText(str(data[0][1]))
            self.ui.lineEdit_2.setText(str(data[0][2]))
            self.ui.lineEdit_3.setText(str(data[0][3]))



    def add(self):
        name = self.ui.lineEdit_1.text()
        login = self.ui.lineEdit_2.text()
        password = self.ui.lineEdit_3.text()
        if self.id:
            self.bd.del_log(self.id)
            self.bd.changelog(self.id,name,login,password)
        else:
            self.bd. add_log(name, login,password)
        self.close()
