from fastapi import APIRouter
from src.Backend.services.analytics_service import AnalyticsService

router = APIRouter(
    prefix="/analytics",
    tags=["Fleet Analytics"]
)


@router.get("")
def analytics():

    return AnalyticsService.get()