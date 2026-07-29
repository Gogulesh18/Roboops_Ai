from fastapi import APIRouter

from src.Backend.services.dashboard_service import DashboardService

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("")
def dashboard():

    return DashboardService.summary()