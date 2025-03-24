import os

from cryptography.fernet import Fernet


class Secrets:
    def __init__(self, key_file: str = "secret.key") -> None:
        self.key_file = key_file
        self.key = self._load_or_generate_key()
        self.cipher = Fernet(self.key)

    def _load_or_generate_key(self) -> bytes:
        if os.path.exists(self.key_file):
            with open(self.key_file, "rb") as key_file:
                return key_file.read()
        key = Fernet.generate_key()
        with open(self.key_file, "wb") as key_file:
            key_file.write(key)
        return key

    def encrypt(self, data: str) -> str:
        return self.cipher.encrypt(data.encode()).decode()

    def decrypt(self, data: str) -> str:
        return self.cipher.decrypt(data.encode()).decode()
