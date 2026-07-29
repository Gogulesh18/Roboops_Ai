from fastapi import APIRouter

from src.Backend.services.simulation_service import SimulationService

router = APIRouter(
    prefix="/simulation",
    tags=["Simulation"]
)


@router.post("/tick")
def tick():

    return SimulationService.tick()