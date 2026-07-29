from pydantic import BaseModel

class DashboardSummary(BaseModel):
    total_robots: int
    working: int
    idle: int
    charging: int
    average_battery: float
    fleet_health_score: int
    active_tasks: list[str]