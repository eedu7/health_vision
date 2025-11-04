from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr = Field(..., title="Email", description="The email address of the user")
    password: str = Field(..., title="Password", description="The password of the user")
