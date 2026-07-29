from fastapi import APIRouter

from src.Backend.services.autopilot_service import AutoPilotService

router = APIRouter(
    prefix="/autopilot",
    tags=["Autopilot"]
)


@router.post("/start")
def start():

    AutoPilotService.start()

    return {
        "message": "Autopilot Started"
    }


@router.post("/stop")
def stop():

    AutoPilotService.stop()

    return {
        "message": "Autopilot Stopped"
    }