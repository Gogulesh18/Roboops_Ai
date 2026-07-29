from fastapi import APIRouter

from src.Backend.agents.coordinator import CoordinatorAgent

router = APIRouter(
    prefix="/coordinator",
    tags=["Coordinator"]
)


@router.get("/report")
def full_report():
    return CoordinatorAgent.run()