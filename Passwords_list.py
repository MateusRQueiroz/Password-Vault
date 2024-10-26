import os
import stat 

''' Initializes a passwords list object.'''
class Passwords_list():
    def __init__(self):
        self.password_book = {}
        self.password_object_list = []
        self.decrypted_password_list = []
    
    ''' Adds a password a file the password_book dictionary, to a password object list, and to a file.
        Ensures that the file can only be written in and read by the owner.'''
    def add_password(self, password): 
        self.password_book[password.platform] = password.encrypted_password
        self.password_object_list.append(password)
        with open('Passwords_List', 'a') as passwords_file: 
            passwords_file.write(f'{password.platform}: {password.encrypted_password.decode()}\n')
        os.chmod('Passwords_List', stat.S_IRUSR | stat.S_IWUSR)
    
    def get_password_book(self):
        return self.password_book
    
    ''' Displays passwords in a separate file'''
    def view_passwords(self, master_password):
        updated_lines = []
        try: 
            with open('Passwords_List', 'r+') as passwords_file:
                lines = passwords_file.readlines() 
                passwords_file.seek(0)
                for line in lines:
                    platform, encrypted_password = line.split(': ', 1)
                    encrypted_password = encrypted_password.strip()
                    for password in self.password_object_list:
                        if password.platform == platform.strip(): 
                            decrypted_password = password.decrypt_password(master_password)
                            updated_lines.append(f'{platform}: {decrypted_password}\n')
                passwords_file.writelines(updated_lines)
                passwords_file.truncate()
        except PermissionError: 
            print("You don't have permission to access this file")
        except Exception as e: 
            print(f'Error {e} occurred')

        
