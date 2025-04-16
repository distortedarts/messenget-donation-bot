import os
from cryptography.fernet import Fernet

FERNET_KEY = os.getenv("FERNET_KEY")
if not FERNET_KEY:
    raise EnvironmentError("FERNET_KEY is missing from environment.")

fernet = Fernet(FERNET_KEY.encode())

def get_credential(key: str) -> str:
    encrypted = os.getenv(key)
    if not encrypted:
        raise KeyError(f"Missing encrypted value for {key}")
    return fernet.decrypt(encrypted.encode()).decode()
