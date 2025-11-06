from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Literal
from uuid import uuid4

from jose import ExpiredSignatureError, JWTError, jwt

from app.core.config import config
from app.schemas.token import Token

BASE_PATH = Path(__file__).parent.parent.parent

TokenType = Literal["access", "refresh"]


class JWTHandler:
    def __init__(self):
        self.private_key = self._load_key(config.JWT_PRIVATE_KEY_PATH)
        self.public_key = self._load_key(config.JWT_PUBLIC_KEY_PATH)
        self.algorithm = config.JWT_ALGORITHM
        self.access_token_expire_minutes = config.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
        self.refresh_token_expire_days = config.JWT_REFRESH_TOKEN_EXPIRE_DAYS

    def _load_key(self, key_path: str) -> str:
        path = Path(key_path)

        if not path.is_absolute():
            path = BASE_PATH / key_path

        with open(path, "r") as key_file:
            return key_file.read()

    def encode(self, payload: Dict[str, Any], token_type: TokenType) -> str:
        payload = payload.copy()
        if token_type == "access":
            expires_in = datetime.now(UTC) + timedelta(minutes=self.access_token_expire_minutes)
        else:
            expires_in = datetime.now(UTC) + timedelta(days=self.refresh_token_expire_days)

        payload.update(
            {"exp": int(expires_in.timestamp()), "type": token_type, "iat": int(datetime.now(UTC).timestamp())}
        )
        return jwt.encode(payload, self.private_key, algorithm=self.algorithm)

    def decode(self, token: str, expected_type: TokenType = None, verify_exp: bool = True) -> Dict[str, Any]:
        try:
            payload = jwt.decode(
                token,
                self.public_key,
                algorithms=[self.algorithm],
                options={"verify_exp": verify_exp},
            )
            if expected_type and payload.get("type") != expected_type:
                raise ValueError(f"Expected {expected_type} token, got {payload.get('type')}")
            return payload
        except ExpiredSignatureError:
            raise ValueError("Token has expired.")
        except JWTError as e:
            raise ValueError(f"Invalid token: {e}")
        except Exception as e:
            raise ValueError(f"An error occurred while decoding the token: {e}")

    def create_token_pair(
        self,
        user_id: str,
        issuer: str,
        roles: List[str] | None = None,
    ) -> Token:
        # Unique token IDs
        access_jti = str(uuid4())
        refresh_jti = str(uuid4())

        # Access Token Payload
        access_payload = {
            "sub": user_id,
            "iss": issuer,
            "roles": roles or [],
            "jti": access_jti,
        }

        # Refresh Token Payload
        refresh_payload = {"sub": user_id, "iss": issuer, "jti": refresh_jti}

        access_token = self.encode(access_payload, token_type="access")
        refresh_token = self.encode(refresh_payload, token_type="refresh")
        return Token(access_token=access_token, refresh_token=refresh_token)
