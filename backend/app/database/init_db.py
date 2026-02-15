from app.database.connection import engine, Base
from app.models import log  # important: import models so tables register


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
