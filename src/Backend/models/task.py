from pydantic import BaseModel


class Task(BaseModel):
    task_id: str
    task_name: str
    priority: str
    destination: str
    status: str = "Waiting"