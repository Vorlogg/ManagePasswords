from PyQt5 import QtWidgets
from model import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QModelIndex, QItemSelectionModel
import sys
from BD import Orm

class InputDialog(QtWidgets.QDialog):
    def __init__(self, root, state):
        super().__init__(root)
        self.win = root
        self.state = state
        label = QtWidgets.QLabel('Введите название')
        self.edit = QtWidgets.QLineEdit()
        button = QtWidgets.QPushButton('Найти')
        button.clicked.connect(self.push)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.edit)
        layout.addWidget(button)
        self.setLayout(layout)
        self.bd = Orm()

    def push(self):
        if self.edit.text():
            r = self.bd.searchLog(self.edit.text())
            if r:
                self.win.now(r)
                self.close()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Не найдено ")
                msg.addButton('Ок', QMessageBox.RejectRole)
                msg.exec()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.state = 1
#        self.ui.pushButton_1.clicked.connect(self.addfac)
      #  self.ui.pushButton_2.clicked.connect(self.addmat)
   #     self.ui.pushButton_3.clicked.connect(self.delmat)
   #     self.ui.pushButton_4.clicked.connect(self.search)
        self.bd = Orm()
        self.bd.addlog()
        self.now(self.bd.allmat())
        self.id = False

    def update(self):
        self.state = 1
        self.now(self.bd.allmat())
        self.ui.pushButton.show()
        self.ui.pushButton_2.show()
        self.ui.pushButton_4.show()
        self.ui.pushButton_6.show()
        self.ui.pushButton_9.hide()
        self.ui.pushButton_5.hide()
        self.ui.pushButton_10.hide()

    def now(self, data):
        if data:
            self.ui.tableWidget.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
            self.ui.pushButton_4.setEnabled(True)
            # ряды и столбцы
            self.ui.tableWidget.setRowCount(
                len(data)
            )
            self.ui.tableWidget.setColumnCount(
                len(data[0])
            )
            self.ui.tableWidget.setHorizontalHeaderLabels(
                    ('Id','Название приложения', 'Пароль',))


            row = 0
            for tup in data:
                col = 0

                for item in tup:
                    cellinfo = QTableWidgetItem(str(item))
                    cellinfo.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                    )
                    self.ui.tableWidget.setItem(row, col, cellinfo)
                    # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(col , QHeaderView.Stretch)

                    col += 1

                row += 1
                self.ui.tableWidget.resizeColumnsToContents()
                self.ui.tableWidget.horizontalHeader().setSectionResizeMode(col - 1, QHeaderView.Stretch)
        else:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(False)

    def addmat(self):
        self.dualog = AddMaterial()
        self.dualog.exec()
        self.now(self.bd.allmat(), self.state)



    def delmat(self):  # проблема с индексами после удаления
        state = self.state
        if state == 1:
            if not self.id:
                self.now(self.bd.allmat(), state)
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Вы не выбрали не одну запись")
                msg.addButton('Ок', QMessageBox.RejectRole)
                msg.exec()
            else:
                self.bd.delLog(self.id)
                self.now(self.bd.allmat(), state)
                self.id = False
        elif state == 2:
            if not self.id:
                self.now(self.bd.allres(), state)
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Вы не выбрали не одну запись")
                msg.addButton('Ок', QMessageBox.RejectRole)
                msg.exec()
            else:
                # print(self.id)
                self.bd.delres(self.id)
                self.now(self.bd.allres(), state)
                self.id = False
        elif state == 3:
            if not self.id:
                self.now(self.bd.allcon(), state)
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Вы не выбрали не одну запись")
                msg.addButton('Ок', QMessageBox.RejectRole)
                msg.exec()
            else:
                # print(self.id)
                self.bd.delcon(self.id)
                self.now(self.bd.allcon(), state)
                self.id = False

    @pyqtSlot(QModelIndex)
    def on_tableWidget_clicked(self, index: QModelIndex):  # получение индекса строки при нажатие
        self.id = int(self.ui.tableWidget.item(index.row(), 0).text())

    @pyqtSlot(QModelIndex)
    def on_tableWidget_doubleClicked(self, index: QModelIndex):  # получение списка обьектов
        r = int(self.ui.tableWidget.item(index.row(), 0).text())
        if self.state == 1:
            data = self.bd.allfac(r)
        elif self.state == 2:
            res = self.bd.getres(r)
            fio = res.name + " " + res.family[0] + ". " + res.patronymic[0] + '.'
            data = self.bd.resfacil(fio)

        elif self.state == 3:
            cons = self.bd.getcons(r)
            data = self.bd.consfacil(cons.facility)
        if not data:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Нет записей")
            msg.addButton('Ок', QMessageBox.RejectRole)
            msg.exec()

        else:
            self.twow = TwoWindow(self, r, self.state)
            self.twow.show()

    def search(self):
        self.ui.pushButton_4.hide()
        self.ui.pushButton_5.show()
        self.search = InputDialog(self, self.state)
        self.search.exec()

    def tomain(self):
        self.ui.pushButton_5.hide()
        if self.state == 1:
            self.update()
        elif self.state == 2:
            self.responsible()
        elif self.state == 3:
            self.constructionObject()







app = QtWidgets.QApplication([])
application = MainWindow()
application.show()

sys.exit(app.exec())