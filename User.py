import json 
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os

class User: 
    # Creates a file called users.json, which will be used to store users login information and passwords. 
    # Initiates self.users variable that will store the user's information outside the json file
    def __init__(self, filename='users.json'):
        self.filename = filename
        self.users = self.load_user_data()

    # Derives a unique key, only accessible through the master password and the salt
    def derive_key(self, master_password, salt): 
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt = salt,
            iterations=10000, )
        key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
        return key
    
    # Verifies if json file exist and, if it does, loads the users information into it.
    # If the file doesn't exist, it returns an empty dictionary
    def load_user_data(self): 
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file: 
                data = json.load(file)
                return data
        else:
            return {}

    # It verifies if username already exists. If it doesn't, it registers the user
    # Generates a random salt value for the user in bytes, that is instantly converted into a string
    # Generates a key for the user, that is derived from the master password and the salt (in bytes)
    # Creates a fernet object with the key
    def register_user(self, username, master_password): 
        if username in self.users: 
            print('\nThis username already exists.')
            return False
        salt = os.urandom(16).hex()
        key = self.derive_key(master_password, bytes.fromhex(salt))
        fernet = Fernet(key)

        # Creates the key username for the self.users dictionary.
        # The key has 3 values: 1) the salt, 2) the hashed password (which is the encryption of the master password using the fernet object),
        # in not-byte format in order to later be added to the json file, and 3) a dictionary that will hold the users encrypted passwords
        self.users[username] = {
            'salt': salt,
            'hashed_password': fernet.encrypt(master_password.encode()).decode(),
            'passwords': {}
        }
        self.save_user_data()
        print('User registered successfully!')

    # Dumps everything that was written about the user in the json file
    def save_user_data(self): 
        with open(self.filename, 'w') as file: 
            json.dump(self.users, file)
