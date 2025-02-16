# Password Manager

Password Manager is a command-line application that allows users to securely store and manage their passwords using encryption. It encrypts passwords using a master password and stores them in a JSON file, ensuring security and persistence.

## Features

- User registration with secure master password storage.
- Secure password encryption using the Fernet symmetric encryption algorithm.
- View and manage stored passwords.
- Persistent storage of passwords using JSON.

## Usage
### Main Menu Options

- `(R)`egister – Create a new user account with a master password.
- `(L)`ogin – Access stored passwords using a master password.
- `(Q)`uit – Exit the application.

### Logged-In Options

- `(1)` Add Password – Save a new password for a platform.
- `(2)` View Passwords – Retrieve and decrypt stored passwords.
- `(3)` Logout – Exit the user session.

## Installation
### Prerequisites

- Python 3.x
- ```cryptography``` library

### Steps

1. Clone this repository:

   ```git clone https://github.com/MateusRQueiroz/Password-Vault.git```

2. Navigate to the project directory:

   ```cd PasswordManager```

3. Install dependencies:

   ```pip install cryptography```

4. Run the application:

   ```python main.py```

## Contributing

- Feel free to fork and submit pull requests!

## Notes

- The master password is never stored in plain text.
- Users must remember their master password, as it cannot be recovered.
- Passwords are encrypted using a key derived from the master password and a unique salt.

## License

This project is licensed under the MIT License.