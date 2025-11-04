import uvicorn

from app.core.config import config

if __name__ == "__main__":
    uvicorn.run(
        "app.core.server:app",
        port=config.PORT,
        host=config.HOST,
        reload=True if config.ENVIRONMENT == "development" else False,
    )
