from peewee import *

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

    def getmat(self, id):
        r = Login.get(Login.id == id)
        return r

    def allLog(self):
        r = []
        for mat in Login.select():
            id = mat.id
            name = mat.name
            login = mat.login
            password = mat.password
            r.append((id,name,login,password))
        return r

    def addlog(self, name,login, password):
        Login.create(name=name,login=login,password=password)

    def delLog(self, id):
        r = Login.get(Login.id == id)
        r.delete_instance(recursive=True)

    def searchLog(self, info):
        r = []
        for log in Login.select().where(Login.name.contains(info)):
            id = log.id
            name = log.name
            login = log.login
            password = log.password
            r.append((id, name,login, password))
        return r
