from pwdlib import PasswordHash


class Password:
    _argon = PasswordHash.recommended()

    @staticmethod
    def hash_password(plain_password: str) -> str:
        """Hash a plain text password using bcrypt."""
        return Password._argon.hash(plain_password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify a plain text password against a hashed password."""
        return Password._argon.verify(plain_password, hashed_password)
