import os

from cryptography.fernet import Fernet


class Secrets:
    def __init__(self, key_file: str = "secret.key") -> None:
        self.key_file = key_file
        self.key = self._load_or_generate_key()  # Load or generate an encryption key
        self.cipher = Fernet(self.key)

    def _load_or_generate_key(self) -> bytes:
        # Load the encryption key from file or generate a new one if not found
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as key_file:
                return key_file.read()
        key = Fernet.generate_key()  # Generate a new key
        with open(self.key_file, "wb") as key_file:
            key_file.write(key)
        return key

    def encrypt(self, data: str) -> str:
        # Encrypt the given data string and return the encrypted string
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, data: str) -> str:
        # Decrypt the given encrypted string and return the original data
        return self.cipher.decrypt(data.encode()).decode()
