from peewee import *

db = SqliteDatabase('bd.db')


class Login(Model):
    name = CharField()
    login = CharField()
    password = CharField()


    class Meta:
        database = db  # модель базы данных


class Orm():
    def __init__(self):
        Login.create_table()

    def getmat(self, id):
        r = Login.get(Login.id == id)
        return r

    def allmat(self):
        r = []
        for mat in Login.select():
            id = mat.id
            name = mat.name
            login = mat.login
            password = mat.password
            r.append((id,name,login,password))
        return r

    def addlog(self, name,login, password):
        Login.create(name=name, password=password,login=login)

    def delLog(self, id):
        r = Login.get(Login.id == id)
        r.delete_instance(recursive=True)

    def searchLog(self, info):
        r = []
        for mat in Login.select().where(Login.name.contains(info)):
            id = mat.id
            name = mat.name
            login = mat.login
            password = mat.password
            r.append((id, name,login, password))
        return r

