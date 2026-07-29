from fastapi import APIRouter

from src.Backend.agents.mission_planner import MissionPlanner

router = APIRouter(
    prefix="/mission",
    tags=["Mission Planner"]
)


@router.post("/{task_name}")
def assign(task_name: str):

    return MissionPlanner.assign_task(task_name)