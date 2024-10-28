import os
import stat 
import time 

''' Initializes a passwords list object.'''
class Passwords_list():
    def __init__(self):
        self.password_book = {}
        self.password_object_list = []
        self.decrypted_password_list = []
    
    ''' Adds a password a file to the password_book dictionary, to a password object list, and to a file.
        Ensures that the file can only be written in and read by the owner.'''
    def add_password(self, password): 
        self.password_book[password.platform] = password.encrypted_password
        self.password_object_list.append(password)
        with open('Passwords_List', 'a') as passwords_file: 
            passwords_file.write(f'{password.platform}: {password.encrypted_password.decode()}\n')
        os.chmod('Passwords_List', stat.S_IRUSR | stat.S_IWUSR)
    
    def get_password_book(self):
        return self.password_book

    ''' Deletes password from the file '''
    def delete_password_from_list(self, password_instance): 
        updated_lines = []
        with open('Passwords_List', 'r+') as passwords_file:
            lines = passwords_file.readlines()
            passwords_file.seek(0)
            for line in lines: 
                if password_instance.platform in line: 
                    continue
                else:
                    updated_lines.append(line)
            for updated_line in updated_lines:
                passwords_file.write(updated_line)
            passwords_file.truncate()
    
    ''' Displays passwords in a separate file'''
    def view_passwords(self, master_password):
        try: 
            updated_lines = []
            with open('Passwords_List', 'r+') as passwords_file:
                lines = passwords_file.readlines() 

            for line in lines:
                platform, encrypted_password = line.split(': ', 1)
                encrypted_password = encrypted_password.strip()
                for password in self.password_object_list:
                    if password.platform == platform.strip(): 
                        decrypted_password = password.decrypt_password(master_password)
                        updated_lines.append(f'{platform}: {decrypted_password}\n')
        
            with open('Passwords_List', 'w') as passwords_file:
                passwords_file.writelines(updated_lines)
                
        except PermissionError: 
            print("You don't have permission to access this file")
        except Exception as e: 
            print(f'Error {e} occurred')
        time.sleep(5)
        self.encrypt_file()

    def encrypt_file(self): 
        updated_lines = []
        with open('Passwords_List', 'r+') as passwords_file: 
            lines = passwords_file.readlines()
            passwords_file.seek(0)
            for line in lines:
                platform, decrypted_password = line.split(': ', 1)
                decrypted_password.strip()
                for password in self.password_object_list:
                    if password.platform == platform.strip(): 
                        encrypted_password = password.encrypted_password
                        updated_lines.append(f'{platform}: {encrypted_password}\n')
            passwords_file.seek(0)
            passwords_file.writelines(updated_lines)
            passwords_file.truncate()
            passwords_file.close()


        
