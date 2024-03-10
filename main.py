from fastapi import FastAPI, Depends
from pydantic import BaseModel

from schemas import STaskAdd

from typing import Optional, Annotated

from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База удалена')
    await create_tables()
    print('База готова')
    yield
    print('Выключение')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)

tasks = []


class Task(BaseModel):
    name: str
    description: Optional[str] = None


