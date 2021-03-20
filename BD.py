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
    def addAdmin(self,password):
        Admin.create(password_admin=self.cr.encrypt(password))
    @staticmethod
    def chekDB():
        return os.path.exists('admin.db')
    def chekPass(self,password):
        r=Admin.get(Admin.id==1)
        if self.cr.decrypt(r.password_admin) == password:
            return True
        else:
            return False

class Orm():
    def __init__(self):
        Login.create_table()
        self.cr=Cryto()

    def getLog(self, id):
        r = Login.get(Login.id == id)
        return r

    def allLog(self):
        r = []
        for log in Login.select():
            id = log.id
            name =log.name
            login =self.cr.decrypt(log.login)
            password =self.cr.decrypt(log.password)
            r.append((id,name,login,password))
        return r
    def getChange(self,id):
        data = Login.get(Login.id == id)
        r=[]
        id = data.id
        name =data.name
        login =self.cr.decrypt(data.login)
        password =self.cr.decrypt(data.password)
        r.append((id,name,login,password))
        return r
    def addlog(self, name,login, password):
        Login.create(name=name,login=self.cr.encrypt(login), password=self.cr.encrypt(password))
    def changelog(self,id, name,login, password):
        Login.create(id=id,name=name,login=self.cr.encrypt(login), password=self.cr.encrypt(password))

    def delLog(self, id):
        r = Login.get(Login.id == id)
        r.delete_instance(recursive=True)

    def searchLog(self, name):
        r = []
        for log in Login.select().where(Login.name.contains(name)):
            id = log.id
            name =log.name
            login = self.cr.decrypt(log.login)
            password = self.cr.decrypt(log.password)
            r.append((id, name,login, password))
        return r

