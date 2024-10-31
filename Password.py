from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

class Password():
    # Initiates a password object with platform, password (that is instantly encrypted), a master_password
    # and a salt (which are instantly transformed into a key)
    def __init__(self, platform, password, master_password, salt):
        self.platform = platform
        self.salt = bytes.fromhex(salt)
        self.key = self.derive_key(master_password, self.salt)
        self.f = Fernet(self.key)
        if password:
            self.encrypted_password = self.encrypt_password(password)
        else: 
            None
        self.decrypted_password = None

    # Derives key from master_password and salt utilizing PBKDF2 and hashes
    # Ensures key is in suitable format. Returns key 
    def derive_key(self, master_password, salt): 
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt = salt,
            iterations=10000, )
        key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
        return key

    # Encrypts password with fernet object (made with key) and returns it.
    def encrypt_password(self, password):
        if self.f is None:
            self.f = Fernet(self.key)
        self.encrypted_password = self.f.encrypt(password.encode()).decode()
        return self.encrypted_password
    
    # Decrypts password utilizing the fernet object
    def decrypt_password(self): 
        try: 
            self.decrypted_password = self.f.decrypt(self.encrypted_password).decode()
            return self.decrypted_password
        except InvalidToken:
            print("The program is unable to decrypt the password")
    
    
    def change_password(self, passwords_list, new_password, master_password):
        pass

    def display_password(self, master_password): 
        pass