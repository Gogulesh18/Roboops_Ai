from fastapi import APIRouter
from src.Backend.services.health_service import HealthService

router = APIRouter(
    prefix="/fleet",
    tags=["Fleet"]
)

@router.get("/health")
def fleet_health():
    return HealthService.calculate()