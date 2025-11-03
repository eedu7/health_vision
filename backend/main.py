import asyncio

from sqlalchemy import text


async def main():
    from app.core.db.session import get_async_session

    async with get_async_session() as session:
        try:
            await session.execute(text("SELECT 1"))
            print("Database connection successful")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False


if __name__ == "__main__":
    asyncio.run(main())
