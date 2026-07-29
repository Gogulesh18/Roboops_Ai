from fastapi import APIRouter

from src.Backend.agents.traffic_agent import TrafficAgent

router = APIRouter(
    prefix="/agents",
    tags=["Agents"]
)


@router.get("/traffic")
def traffic_analysis():
    return TrafficAgent.analyze()