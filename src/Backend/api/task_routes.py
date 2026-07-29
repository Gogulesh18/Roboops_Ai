from fastapi import APIRouter

from src.Backend.models.task import Task
from src.Backend.services.task_queue_service import TaskQueueService

router = APIRouter(
    prefix="/tasks",
    tags=["Task Queue"]
)


@router.get("")
def tasks():
    return TaskQueueService.get_all()


@router.post("")
def create_task(task: Task):

    TaskQueueService.add(task)

    return {
        "message": "Task added successfully",
        "task": task
    }