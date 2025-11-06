import re

from pydantic import BaseModel, EmailStr, Field, field_validator

from .token import Token
from .user import UserOut


class UserBase(BaseModel):
    email: EmailStr = Field(
        ..., title="Email", description="The email address of the user", examples=["john.doe@gmail.com"]
    )
    password: str = Field(
        ...,
        min_length=16,
        max_length=64,
        title="Password",
        description="The password of the user",
        examples=["Password@12345678"],
    )


class UserCreate(UserBase):
    @field_validator("password")
    def validate_password(cls, value: str) -> str:
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not re.search(r"[0-9]", value):
            raise ValueError("Password must contain at least one digit.")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Password must contain at least one special character.")

        return value


class UserLogin(UserBase):
    pass


class AuthResponse(BaseModel):
    user: UserOut
    token: Token
