from cryptography.fernet import Fernet
class Cryto():
    def __init__(self):
        self.key=b'3rDAX513WNIwq6mOMEvFtgpJBhDsm8vQPb_OwwwCNPg='
        self.cipher= Fernet(self.key)
    def encrypt(self,data):
        return self.cipher.encrypt(data.encode('utf-8')).decode('utf-8')
    def decrypt(self,data):
        return self.cipher.decrypt(data.encode('utf-8')).decode('utf-8')
    def generate(self):
        return Fernet.generate_key()

# cr=Cryto()
# c=cr.encrypt('hello')
# print(c)
# r=cr.decrypt(c)
# print(r)