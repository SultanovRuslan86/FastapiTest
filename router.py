from fastapi import APIRouter, Depends

from typing import Optional, Annotated
from schemas import STaskAdd, STask, STaskID
from repository import TaskRepository

router = APIRouter(
    prefix='/tasks',
    tags=['Задания'],
)


@router.post('')
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}


@router.get('')
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks


# @app.get("/home")
# def get_home():
#     return {"data": 'Hello world !!!'}