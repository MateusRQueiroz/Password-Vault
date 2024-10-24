from cryptography.fernet import Fernet
from Password import Password
from Passwords_list import Passwords_list

password1 = Password('Facebook', '1234', '321')
password2 = Password('Twitter', '1234124', '321')
password3 = Password('Crunchyroll', '0312', '321')
password4 = Password('Netflix', '3213214', '321')

password1.encrypt_password()
password2.encrypt_password()
password3.encrypt_password()
password4.encrypt_password()



passwords_list1 = Passwords_list()


passwords_list1.add_password(password4)
passwords_list1.add_password(password2)
passwords_list1.add_password(password3)
passwords_list1.add_password(password1)

passwords_list1.view_passwords('321')