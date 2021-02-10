from cryptography.fernet import Fernet, InvalidToken


class Cryptography:
    def __init__(self, file='secret.key'):
        self.file = file
        self.key = self.get_create_key()

    def get_create_key(self):
        """Loads a key from a file or creates a new key and saves that key to a new file."""
        try:
            key = bytes(self.load_key())
        except FileNotFoundError:
            key = bytes(self.generate_key())
        return key

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.file, 'wb') as key_file:
            key_file.write(key)
            print(f'Exported key to "{self.file}"')
        return key

    def load_key(self):
        return open(self.file, 'rb').read()

    def encrypt_message(self, raw_message):
        encoded_message = raw_message.encode()
        encrypted_message = Fernet(self.key).encrypt(encoded_message)
        return encrypted_message

    def decrypt_message(self, encrypted_message):
        try:
            fern = Fernet(self.key)
            decrypted_message = fern.decrypt(encrypted_message).decode()
            return decrypted_message
        except InvalidToken:
            print('Token not found.\n'
                  'Please save a token as a txt file and enter the file name on object creation.')
