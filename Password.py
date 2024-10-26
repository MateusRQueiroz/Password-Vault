from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

class Password():
    def __init__(self, platform, password, master_password):
        self.platform = platform
        self.salt = os.urandom(16)
        self.key = self.derive_key(master_password)
        self.f = Fernet(self.key)
        self.encrypted_password = self.encrypt_password(password)
        self.decrypted_password = None

    def derive_key(self, master_password): 
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt = self.salt,
            iterations=10000, )
        self.key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
        return self.key

    def encrypt_password(self, password):
        if self.f is None:
            self.f = Fernet(self.key)
        self.encrypted_password = self.f.encrypt(password.encode())
        return self.encrypted_password
    
    def decrypt_password(self, master_password): 
        self.derive_key(master_password)
        try: 
            self.decrypted_password = self.f.decrypt(self.encrypted_password).decode()
            return self.decrypted_password
        except InvalidToken:
            print("The program is unable to decrypt the password")
    
    def change_password(self, passwords_list, new_password, master_password):
        try: 
            if self.decrypt_password(master_password):
                passwords_list.password_book[self.platform] = self.encrypt_password(new_password)
                print("Password successfully changed")
        except:
            print("Unable to change the password")

    def remove_password(self, password_book): 
        del password_book[self.platform]

    def display_password(self, master_password): 
        self.decrypted_password = self.decrypt_password(master_password)
        print(self.decrypted_password)