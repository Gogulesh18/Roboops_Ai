from fastapi import APIRouter, HTTPException

from src.Backend.models.robot import Robot
from src.Backend.services.fleet_service import FleetService

router = APIRouter(prefix="/robots", tags=["Robots"])


@router.get("")
def get_all_robots():
    return FleetService.get_all_robots()


@router.get("/{robot_id}")
def get_robot(robot_id: str):

    robot = FleetService.get_robot(robot_id)

    if robot is None:
        raise HTTPException(
            status_code=404,
            detail="Robot not found"
        )

    return robot


@router.post("")
def add_robot(robot: Robot):
    return FleetService.add_robot(robot)