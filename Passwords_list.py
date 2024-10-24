
class Passwords_list():
    def __init__(self):
        self.password_book = {}
        self.password_object_list = []
        self.decrypted_password_list = []
    
    def add_password(self, password): 
        self.password_book[password.platform] = password.encrypt_password()
        self.password_object_list.append(password)
        with open('Passwords_List', 'a') as passwords_file: 
            passwords_file.write(f'{password.platform}: {self.password_book[password.platform]}\n')
    
    def get_password_book(self):
        return self.password_book
    
    def view_passwords(self, master_password):
        with open('Passwords_List', 'r+') as passwords_file:
            lines = passwords_file.readlines() 
            passwords_file.seek(0)
            updated_lines = []
            for line in lines:
                platform, encrypted_password = line.split(': ', 1)
                encrypted_password = encrypted_password.strip()
                for password in self.password_object_list:
                    if password.platform == platform.strip(): 
                        decrypted_password = password.decrypt_password(master_password)
                        updated_lines.append(f'{platform}: {decrypted_password}\n')
            passwords_file.writelines(updated_lines)
            passwords_file.truncate()
        
