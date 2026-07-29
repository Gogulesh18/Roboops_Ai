from fastapi import APIRouter
from src.Backend.services.collision_service import CollisionService

router = APIRouter(
    prefix="/collision",
    tags=["Collision Detection"]
)


@router.get("/")
def detect():

    return CollisionService.detect()