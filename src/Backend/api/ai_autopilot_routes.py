from fastapi import APIRouter

from src.Backend.services.ai_decision_service import AIDecisionService
from src.Backend.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/ai",
    tags=["AI Autopilot"]
)


@router.post("/autopilot")
def autopilot():

    decision = AIDecisionService.decide()

    dashboard = DashboardService.summary()

    return {
        "success": True,
        "decision": decision,
        "dashboard": dashboard
    }