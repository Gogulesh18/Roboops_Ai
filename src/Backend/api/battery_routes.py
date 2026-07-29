from fastapi import APIRouter

from src.Backend.agents.battery_agent import BatteryAgent

router = APIRouter(
    prefix="/agents",
    tags=["Agents"]
)


@router.get("/battery")
def battery_analysis():
    return BatteryAgent.analyze()
