import base64
import os
from cryptography.fernet import Fernet, InvalidToken

class CipherModel:
    def __init__(self, phrase: str = "", token1: str = None, token2: str = None):
        self.phrase = phrase
        self.token1 = token1 or self._generate_token()
        self.token2 = token2 or self._generate_token()
        self.fernet1 = Fernet(self.token1.encode())
        self.fernet2 = Fernet(self.token2.encode())

    def _generate_token(self) -> str:
        return base64.urlsafe_b64encode(os.urandom(32)).decode()

    def encrypt(self) -> str:
        encrypted1 = self.fernet1.encrypt(self.phrase.encode())
        encrypted2 = self.fernet2.encrypt(encrypted1)
        return encrypted2.decode()

    def verify(self, encrypted2: str) -> bool:
        try:
            decrypted1 = self.fernet2.decrypt(encrypted2.encode())
            decrypted_phrase = self.fernet1.decrypt(decrypted1).decode()
            return decrypted_phrase == self.phrase
        except Exception:
            return False

    def decrypt(self, encrypted2: str) -> str:
        decrypted1 = self.fernet2.decrypt(encrypted2.encode())
        decrypted_phrase = self.fernet1.decrypt(decrypted1).decode()
        return decrypted_phrase
