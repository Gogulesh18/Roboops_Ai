from src.Backend.services.fleet_service import FleetService
from src.Backend.services.health_service import HealthService
from src.Backend.services.collision_service import CollisionService
from src.Backend.services.task_queue_service import TaskQueueService
from src.Backend.services.analytics_service import AnalyticsService
from src.Backend.services.event_service import EventService


class DashboardService:

    @staticmethod
    def summary():

        robots = FleetService.get_all_robots()

        total = len(robots)

        charging = sum(1 for r in robots if r.status == "Charging")
        working = sum(1 for r in robots if r.status == "Working")
        idle = sum(1 for r in robots if r.status == "Idle")

        # -----------------------------
        # Fleet KPIs
        # -----------------------------

        fleet_utilization = round(
            (working / total) * 100,
            2
        ) if total else 0

        charging_percentage = round(
            (charging / total) * 100,
            2
        ) if total else 0

        idle_percentage = round(
            (idle / total) * 100,
            2
        ) if total else 0

        avg_battery = round(
            sum(r.battery for r in robots) / total,
            2
        ) if total else 0

        average_temperature = round(
            sum(r.temperature for r in robots) / total,
            2
        ) if total else 0

        low_battery = sum(
            1
            for robot in robots
            if robot.battery < 20
        )

        maintenance_needed = sum(
            1
            for robot in robots
            if robot.temperature > 75
        )

        # -----------------------------
        # Fleet Health
        # -----------------------------

        health = HealthService.calculate()["fleet_health_score"]

        # -----------------------------
        # Analytics
        # -----------------------------

        analytics = AnalyticsService.get()

        # -----------------------------
        # Recent Events
        # -----------------------------

        events = EventService.get_all()
        recent_events = events[-5:]

        # -----------------------------
        # Active Tasks
        # -----------------------------

        tasks = list(
            set(
                robot.task
                for robot in robots
                if robot.status != "Idle"
            )
        )

        # -----------------------------
        # Queue / Collision
        # -----------------------------

        collisions = len(CollisionService.detect())
        queued_tasks = len(TaskQueueService.get_all())

        if collisions == 0:
            traffic = "Low"
        elif collisions <= 2:
            traffic = "Medium"
        else:
            traffic = "High"

        # -----------------------------
        # Robot Details
        # -----------------------------

        robot_data = [
            {
                "id": robot.robot_id,
                "status": robot.status,
                "task": robot.task,
                "battery": robot.battery,
                "location": robot.location,
                "temperature": robot.temperature,
                "destination": robot.destination,
                "speed": robot.speed,
                "task_progress": robot.task_progress,
                "estimated_ticks": robot.estimated_ticks,
                "route": robot.route
            }
            for robot in robots
        ]
        # -----------------------------
        # Dashboard Response
        # -----------------------------

        return {

            # Fleet Status
            "total_robots": total,
            "working": working,
            "charging": charging,
            "idle": idle,

            # Fleet KPIs
            "fleet_utilization": fleet_utilization,
            "charging_percentage": charging_percentage,
            "idle_percentage": idle_percentage,
            "average_battery": avg_battery,
            "average_temperature": average_temperature,
            "low_battery_robots": low_battery,
            "maintenance_needed": maintenance_needed,

            # Fleet Health
            "fleet_health_score": health,

            # Tasks
            "active_tasks": tasks,
            "queued_tasks": queued_tasks,

            # Safety
            "collisions": collisions,
            "traffic_level": traffic,

            # Analytics
            "missions_assigned": analytics["missions_assigned"],
            "tasks_completed": analytics["tasks_completed"],
            "failures": analytics["failures"],
            "distance_travelled": analytics["distance_travelled"],
            "collisions_total": analytics["collisions"],

            # Recent Activity
            "recent_events": recent_events,

            # Robot Details
            "robots": robot_data
        }