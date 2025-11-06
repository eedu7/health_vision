from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware

CORS_MIDDLEWARE = Middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
