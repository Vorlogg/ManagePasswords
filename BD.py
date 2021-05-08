from peewee import *
from crypto import Cryto
import os.path

db = SqliteDatabase('bd.db')
admin = SqliteDatabase('admin.db')


class Admin(Model):
    password_admin = CharField()

    class Meta:
        database = admin


class Login(Model):
    name = CharField()
    login = CharField()
    password = CharField()

    class Meta:
        database = db


class AdminPassword():
    def __init__(self):
        Admin.create_table()
        self.cr = Cryto()

    def add_admin(self, password):
        Admin.create(password_admin=self.cr.encrypt(password))

    @staticmethod
    def chek_db():
        return os.path.exists('admin.db')

    def chek_password(self, password):
        r = Admin.get(Admin.id == 1)
        if self.cr.decrypt(r.password_admin) == password:
            return True
        else:
            return False


class Orm():
    def __init__(self):
        Login.create_table()
        self.cr = Cryto()

    def get_log(self, id):
        r = Login.get(Login.id == id)
        return r

    def all_log(self):
        r = []
        for log in Login.select():
            id = log.id
            name = log.name
            login = self.cr.decrypt(log.login)
            password = self.cr.decrypt(log.password)
            r.append((id, name, login, password))
        return r

    def get_change(self, id):
        data = Login.get(Login.id == id)
        r = []
        id = data.id
        name = data.name
        login = self.cr.decrypt(data.login)
        password = self.cr.decrypt(data.password)
        r.append((id, name, login, password))
        return r

    def add_log(self, name, login, password):
        Login.create(name=name, login=self.cr.encrypt(login), password=self.cr.encrypt(password))

    def changelog(self, id, name, login, password):
        Login.create(id=id, name=name, login=self.cr.encrypt(login), password=self.cr.encrypt(password))

    def del_log(self, id):
        r = Login.get(Login.id == id)
        r.delete_instance(recursive=True)

    def search_log(self, name):
        r = []
        for log in Login.select().where(Login.name.contains(name)):
            id = log.id
            name = log.name
            login = self.cr.decrypt(log.login)
            password = self.cr.decrypt(log.password)
            r.append((id, name, login, password))
        return r
