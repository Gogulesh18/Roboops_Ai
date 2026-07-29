from pydantic import BaseModel


class Robot(BaseModel):
    robot_id: str
    battery: int
    location: str
    status: str

    task: str
    destination: str
    speed: float
    temperature: float

    task_progress: int = 0
    estimated_ticks: int = 5

    route: list[str] = []
    route_index: int = 0