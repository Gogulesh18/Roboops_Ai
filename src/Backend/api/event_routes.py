from fastapi import APIRouter

from src.Backend.services.event_service import EventService

router = APIRouter(
    prefix="/events",
    tags=["Fleet Events"]
)


@router.get("")
def events():

    return EventService.get_all()