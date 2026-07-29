from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.Backend.api.robot_routes import router as robot_router
from src.Backend.api.battery_routes import router as battery_router
from src.Backend.api.traffic_routes import router as traffic_router
from src.Backend.api.coordinator_routes import router as coordinator_router
from src.Backend.api.maintenance_routes import router as maintenance_router
from src.Backend.api.dashboard_routes import router as dashboard_router
from src.Backend.api.report_routes import router as report_router
from src.Backend.api.simulation_routes import router as simulation_router
from src.Backend.api.health_routes import router as health_router
from src.Backend.api.mission_routes import router as mission_router
from src.Backend.api.task_routes import router as task_router
from src.Backend.api.collision_routes import router as collision_router
from src.Backend.api.event_routes import router as event_router
from src.Backend.api.analytics_routes import router as analytics_router
from src.Backend.api.ai_routes import router as ai_router
from src.Backend.api.ai_autopilot_routes import router as ai_autopilot_router
from src.Backend.api.autopilot_control_routes import router as autopilot_router
from src.Backend.api.websocket_routes import router as websocket_router




app = FastAPI(
    title="RoboOps AI",
    version="1.0.0",
    description="AI Powered Fleet Operations Platform"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(robot_router)
app.include_router(battery_router)
app.include_router(traffic_router)
app.include_router(coordinator_router)
app.include_router(maintenance_router)
app.include_router(dashboard_router)
app.include_router(report_router)
app.include_router(simulation_router)
app.include_router(health_router)
app.include_router(mission_router)
app.include_router(task_router)
app.include_router(collision_router)
app.include_router(event_router)
app.include_router(analytics_router)
app.include_router(ai_router)
app.include_router(ai_autopilot_router)
app.include_router(autopilot_router)
app.include_router(websocket_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to RoboOps AI 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }       