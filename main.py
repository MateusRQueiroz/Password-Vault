from cryptography.fernet import Fernet
from Password import Password
from Passwords_list import Passwords_list
from User import User
from tkinter import *
from PIL import Image, ImageTk

def main():
    window = Tk()
    window.title('Password Vault')
    icon = PhotoImage(file='lock photo.png')
    window.iconphoto(False, icon)
    window.config(background="light grey")
    window.geometry('500x500')

    label = Label(window, bg='light grey')
    label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    image = Image.open('lock photo.png')
    resized_image = image.resize((300, 300), Image.LANCZOS)
    new_image = ImageTk.PhotoImage(resized_image)

    label.config(image=new_image)
    label.image = new_image 

    username_label = Label(window, text='Username', bg='light grey')
    username_label.grid(row=1, column=1, padx=5, pady=10)

    master_password_label = Label(window, text='Master Password', bg='light grey')
    master_password_label.grid(row=2, column=1, padx=5, pady=10)

    username_entry = Entry(window, bg='dark grey')
    username_entry.grid(row=1, column=2, padx=5, pady=10)

    master_password_entry = Entry(window, show='*', bg='dark grey')
    master_password_entry.grid(row=2, column=2, padx=5, pady=10)

    register_button = Button(window, text='Register', padx=5, pady=5)
    register_button.grid(column=1, row=3, padx=5, pady=10)

    login_button = Button(window, text='Login', padx=5, pady=5)
    login_button.grid(column=2, row=3, padx=5, pady=10)

    window.mainloop()
  
    # Generates a User object, which creates a json file and stores the contents of that file in a users (dictionary)
    user_file = User()
    user = True
    while user: 
        user_action = input('\nWould you like to (R)egister, (L)ogin, or (Q)uit? ')
        # User wants to register
        if user_action == 'R': 
            username = input('\nEnter an username: ')
            master_password = input('\nEnter a master password: ')
            user_file.register_user(username, master_password)
        # User wants to log-in 
        elif user_action == 'L': 
            username = input('\nEnter your username: ')
            master_password = input('\nEnter master password: ')
            # Retrieves user's information from users (dictionary)
            user_data = user_file.users.get(username)
            if user_data: 
                # Sets salt equal to stored salt in the dictionary, and derives the key from master password and the given salt
                salt = user_data['salt']
                key = user_file.derive_key(master_password, bytes.fromhex(salt))
                # Creates fernet object from key
                fernet = Fernet(key)
                try: 
                    # Verifies whether the master password is correct through trying to decrypt the hashed password
                    fernet.decrypt(user_data['hashed_password'].encode())
                    print('Login successful!')
                    # Creates a Passwords_list object with the user_data, which will store the 'passwords' key of user data in a separate dictionary
                    passwords_list = Passwords_list(user_data)
                    login = True
                    while login == True: 
                        user_action = input('''\nWould you like to: 
1) Add Password
2) View Passwords
3) Logout\n''')
                        if user_action == "1": 
                            platform = input('Enter platform: ')
                            password = input('Enter password: ')
                            new_password = Password(platform, password, master_password, salt)
                            passwords_list.add_password(new_password)
                            # Stores the contents of the updated password_book
                            user_data['passwords'] = passwords_list.password_book
                            # Dumps all updates into json file
                            user_file.save_user_data()
                        elif user_action == "2": 
                            passwords_list.view_passwords(master_password, salt)
                        elif user_action == "3": 
                            login = False
                except Exception as e:
                    print(e)
            else: 
                print('User not recognized.')
        elif user_action == 'Q':
            user = False
if __name__ == "__main__":
    main()






