from fastapi import APIRouter

from src.Backend.services.ai_supervisor import AISupervisor

router = APIRouter(
    prefix="/ai",
    tags=["AI Supervisor"]
)


@router.get("/report")
def report():

    return AISupervisor.generate()