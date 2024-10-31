from Password import Password 

class Passwords_list():
    # Creates a separate dictionary to store the users_data dictionary key of passwords (which includes a nested dictionary platforms and encrypted passwords)
    def __init__(self, users_data):
        self.password_book = users_data.get('passwords', {})
    
    # Receives a password object 
    # Accesses the object's encrypted password and stores it in the password_book dictionary
    def add_password(self, password): 
        self.password_book[password.platform] = password.encrypted_password
        print(f'Password for {password.platform} added successfully.')

    def delete_password_from_list(self): 
        pass
    
    # Receives the user's master password and unique salt 
    # Separates the platforms from the encrypted passwords in the password_book objects, iterating through them
        # For each iteration, it creates a new Password object instance, using the platform, master password and salt 
        # Assigns a value to the encrypted password of the Password object equal to the encrypted password of the corresponding password in the password book
        # If the program is able to decrypt the Password object's new encrypted password, it will print the platform and decrypted object for that iteration
    def view_passwords(self, master_password, salt):
        for platform, encrypted_password in self.password_book.items():
            password_instance = Password(platform, None, master_password, salt)
            password_instance.encrypted_password = encrypted_password
            if password_instance.decrypt_password(): 
                print(f'{platform}: {password_instance.decrypt_password()}')
            else:
                print(f'Failed to decrypt password for {platform}')


