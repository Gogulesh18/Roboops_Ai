from fastapi import APIRouter

from src.Backend.agents.maintenance_agent import MaintenanceAgent

router = APIRouter(
    prefix="/agents",
    tags=["Agents"]
)


@router.get("/maintenance")
def maintenance():
    return MaintenanceAgent.analyze()