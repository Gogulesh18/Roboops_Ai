from uuid import uuid4

from src.Backend.models.task import Task
from src.Backend.services.event_service import EventService
from src.Backend.services.fleet_service import FleetService
from src.Backend.services.task_queue_service import TaskQueueService
from src.Backend.services.route_planner import RoutePlanner
from src.Backend.services.robot_selector import RobotSelector
from src.Backend.services.analytics_service import AnalyticsService



class MissionPlanner:

    @staticmethod
    def assign_task(task_name: str):

        robots = FleetService.get_all_robots()

        print("\n========== MISSION PLANNER ==========")

        for robot in robots:

            print(
                f"{robot.robot_id} | "
                f"Status={robot.status} | "
                f"Battery={robot.battery} | "
                f"Temp={robot.temperature} | "
                f"Location={robot.location}"
            )

        destination = "Dispatch"

        best_robot = RobotSelector.select_best_robot(destination)

        print(f"\nSelected Robot : {best_robot}")

        # No robot available
        if best_robot is None:

            task = Task(
                task_id=str(uuid4()),
                task_name=task_name,
                priority="Medium",
                destination="Warehouse Zone",
                status="Waiting"
            )

            TaskQueueService.add(task)

            # ✅ Event Log
            EventService.log(
                "Task Queued",
                "SYSTEM",
                task_name
            )

            print("No robot available. Task queued.")

            return {
                "success": False,
                "message": "No robot available. Task added to queue.",
                "queued_task": task
            }

        # -----------------------------
        # Assign Task
        # -----------------------------

        best_robot.status = "Working"
        best_robot.task = task_name
        best_robot.destination = destination

        best_robot.task_progress = 0
        best_robot.estimated_ticks = 5

        # Generate Route
        route = RoutePlanner.calculate(
            best_robot.location,
            best_robot.destination
        )

        print(f"\nRoute Generated : {route}")

        best_robot.route = route
        best_robot.route_index = 0

        print(f"Route Stored    : {best_robot.route}")
        print(f"Route Index     : {best_robot.route_index}")

        # ✅ Event Log
        EventService.log(
            "Mission Assigned",
            best_robot.robot_id,
            task_name
        )

        print("=====================================\n")

        AnalyticsService.increment(
            "missions_assigned"
        )

        return {
            "success": True,
            "message": f"Task '{task_name}' assigned successfully.",
            "robot": best_robot
        }