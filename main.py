import sys

from PyQt6.QtCore import pyqtSignal, pyqtSlot, QModelIndex
from PyQt6.QtWidgets import *

from BD import Orm, AdminPassword
from add_pass import AddPass
from model import *


class InputDialog(QtWidgets.QDialog):
    def __init__(self, root):
        super().__init__(root)
        self.win = root
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
            r = self.bd.search_log(self.edit.text())
            if r:
                self.win.now(r)
                self.close()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Не найдено ")
                msg.addButton('Ок', QMessageBox.ButtonRole.RejectRole)
                msg.exec()


class AdminDialog(QtWidgets.QDialog):
    runMainWindow = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        if not AdminPassword.chek_db():
            label = QtWidgets.QLabel('Укажите пароль для доступа')
            self.chekAdmin = False
        else:
            label = QtWidgets.QLabel('Введите пароль')
            self.chekAdmin = True
            self.adb = AdminPassword()
        self.edit = QtWidgets.QLineEdit()
        button = QtWidgets.QPushButton('Ок')
        button.clicked.connect(self.push)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(self.edit)
        layout.addWidget(button)
        self.setLayout(layout)
        self.bd = Orm()

    @pyqtSlot()
    def push(self):
        if self.chekAdmin:
            if self.adb.chek_password(self.edit.text()):
                self.runMainWindow.emit()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Неправильный пароль ")
                msg.addButton('Ок', QMessageBox.ButtonRole.RejectRole)
                msg.exec()
        else:
            if self.edit.text():
                self.adb = AdminPassword()
                self.adb.add_admin(self.edit.text())
                self.close()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Пустая строка")
                msg.addButton('Ок', QMessageBox.ButtonRole.ButtonRole.RejectRole)
                msg.exec()


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.pushButton_1.clicked.connect(self.add_log)
        self.ui.pushButton_2.clicked.connect(self.del_log)
        self.ui.pushButton_3.clicked.connect(self.search)
        self.ui.pushButton_4.clicked.connect(self.to_main)
        self.ui.pushButton_5.clicked.connect(self.change_data)
        self.ui.pushButton_4.hide()
        self.id = False
        self.bd = Orm()
        self.now(self.bd.all_log())

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
                ('Id', 'Название приложения', 'Логин', 'Пароль',))
            row = 0
            for tup in data:
                col = 0

                for item in tup:
                    cellinfo = QTableWidgetItem(str(item))
                    cellinfo.setFlags(
                        QtCore.Qt.ItemFlags.ItemIsSelectable | QtCore.Qt.ItemFlags.ItemIsEnabled
                    )
                    self.ui.tableWidget.setItem(row, col, cellinfo)

                    col += 1

                row += 1
                self.ui.tableWidget.resizeColumnsToContents()
                # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(col - 1, QHeaderView.stretchSectionCount)
                self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)

        else:
            self.ui.tableWidget.clear()
            self.ui.tableWidget.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)
            self.ui.pushButton_4.setEnabled(False)

    def add_log(self):

        self.dualog = AddPass()
        self.dualog.exec()
        self.now(self.bd.all_log())

    def change_data(self):
        if not self.id:
            self.now(self.bd.all_log())
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Вы не выбрали не одну запись")
            msg.addButton('Ок', QMessageBox.ButtonRole.RejectRole)
            msg.exec()
        else:
            self.dualog = AddPass(self.id)
            self.dualog.exec()
            self.now(self.bd.all_log())
            self.id = False

    def del_log(self):
        if not self.id:
            self.now(self.bd.all_log())
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Вы не выбрали не одну запись")
            msg.addButton('Ок', QMessageBox.ButtonRole.RejectRole)
            msg.exec()
        else:
            self.bd.del_log(self.id)
            self.now(self.bd.all_log())
            self.id = False

    @pyqtSlot(QModelIndex)
    def on_tableWidget_clicked(self, index: QModelIndex):  # получение индекса строки при нажатие
        self.id = int(self.ui.tableWidget.item(index.row(), 0).text())

    @pyqtSlot(QModelIndex)
    def on_tableWidget_doubleClicked(self, index: QModelIndex):  # получение списка обьектов
        r = self.ui.tableWidget.item(index.row(), index.column()).text()
        clipboard.setText(r)

    def search(self):
        self.ui.pushButton_3.hide()
        self.ui.pushButton_4.show()
        self.search_dialog = InputDialog(self)
        self.search_dialog.exec()

    def to_main(self):
        self.ui.pushButton_4.hide()
        self.ui.pushButton_3.show()
        self.now(self.bd.all_log())


class Factory(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.mainWindow = MainWindow()
        self.adminDialog = AdminDialog()
        self.adminDialog.runMainWindow.connect(self.runMainWindow)
        self.adminDialog.show()

    def runMainWindow(self):
        self.adminDialog.close()
        self.mainWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    clipboard = app.clipboard()
    application = Factory()
    sys.exit(app.exec())
