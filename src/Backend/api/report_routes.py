from fastapi import APIRouter

from src.Backend.agents.coordinator import CoordinatorAgent
from src.Backend.services.report_service import ReportService

router = APIRouter(
    prefix="/report",
    tags=["AI Report"]
)


@router.get("")
def report():

    report = CoordinatorAgent.run()

    return {
        "analysis": ReportService.generate(report)
    }