from cryptography.fernet import Fernet
from Password import Password
from Passwords_list import Passwords_list

passwords_list = Passwords_list()
password_objects = {}

if __name__ == "__main__":
    username = input('''
    This is a safe password manager. \n             
    Username: ''')
    master_password = input('''    Master Password: ''')
    user = True

    while user == True: 
        user_command = int(input('''

        1) Add Password
        2) Change Password
        3) Remove Password
        4) View Password
        5) View Password List

    Select a number: '''))

        if user_command == 1:
            platform = input('\nPlatform: ')
            password = input('Password: ')
            password_object  = Password(platform, password, master_password)
            passwords_list.add_password(password_object)
            password_objects[platform] = password_object

        elif user_command == 2: 
            platform = input('\nPlatform: ')
            new_password = input('New Password: ')
            password_objects[platform].change_password(passwords_list, new_password, master_password)

        elif user_command == 3: 
            platform = input('\nPlatform: ')
            passwords_list.delete_password_from_list(password_objects[platform])
        
        elif user_command == 4: 
            platform = input('\nPlatform: ')
            print(password_objects[platform].decrypt_password(master_password))
        
        elif user_command == 5:
            passwords_list.view_passwords(master_password)
        
        answer = input('''\n Do you want to continue? ''').lower()
        if answer == 'yes':
            user = True
        else:
            user = False