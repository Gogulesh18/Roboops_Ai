import asyncio

from fastapi import APIRouter, WebSocket, WebSocketDisconnect

from src.Backend.services.dashboard_service import DashboardService
from src.Backend.services.websocket_manager import manager

router = APIRouter(tags=["WebSocket"])


@router.websocket("/ws/fleet")
async def fleet_socket(websocket: WebSocket):

    await manager.connect(websocket)

    try:

        while True:

            dashboard = DashboardService.summary()

            await websocket.send_json(dashboard)

            await asyncio.sleep(2)

    except WebSocketDisconnect:

        manager.disconnect(websocket)