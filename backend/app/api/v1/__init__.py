from fastapi import APIRouter

from .auth import auth_router
from .email_verification import email_verification_router
from .password import password_router
from .user import user_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(email_verification_router, prefix="/email-verification", tags=["Email Verification"])
router.include_router(password_router, prefix="/password", tags=["Password Management"])
router.include_router(user_router, prefix="/users", tags=["User Management"])
