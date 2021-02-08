from peewee import *
from crypto import Cryto
db = SqliteDatabase('bd.db')


class Login(Model):
    name = CharField()
    login = CharField()
    password = CharField()
    class Meta:
        database = db


class Orm():
    def __init__(self):
        Login.create_table()
        self.cr=Cryto()

    def getmat(self, id):
        r = Login.get(Login.id == id)
        return r

    def allLog(self):
        r = []
        for log in Login.select():
            id = log.id
            name =self.cr.decrypt(log.name)
            login =self.cr.decrypt(log.login)
            password =self.cr.decrypt(log.password)
            r.append((id,name,login,password))
        return r
    def addlog(self, name,login, password):
        Login.create(name=self.cr.encrypt(name),login=self.cr.encrypt(login), password=self.cr.encrypt(password))

    def delLog(self, id):
        r = Login.get(Login.id == id)
        r.delete_instance(recursive=True)

    def searchLog(self, info):
        r = []
        for log in Login.select().where(Login.name.contains(info)):
            id = log.id
            name = self.cr.decrypt(log.name)
            login = self.cr.decrypt(log.login)
            password = self.cr.decrypt(log.password)
            r.append((id, name,login, password))
        return r
