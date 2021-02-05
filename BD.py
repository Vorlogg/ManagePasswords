from peewee import *

db = SqliteDatabase('bd.db')


class Login(Model):
    name = CharField()
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
            password = mat.password
            r.append((id,name,password))
        return r

    def addlog(self, name, company, store, supplier, reckoning, ndc, count, measure, price):
        Login.create(name=name, company=company, store=store, supplier=supplier, reckoning=reckoning, ndc=ndc,
                     count=count, allCount=count, measure=measure, price=price, allprice=count * price)

    def delmat(self, id):
        r = Login.get(Login.id == id)
        r.delete_instance(recursive=True)

    def search_mater(self, info):
        r = []
        for mat in Login.select().where(Login.name.contains(info)):
            id = mat.id
            name = mat.name
            password = mat.password
            r.append((id, name, password))
        return r

