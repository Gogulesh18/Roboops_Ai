import random

from src.Backend.models import robot
from src.Backend.services.fleet_service import FleetService
from src.Backend.services.task_queue_service import TaskQueueService
from src.Backend.services.navigation_service import NavigationService
from src.Backend.services.traffic_manager import TrafficManager
from src.Backend.services.failure_service import FailureService
from src.Backend.services.event_service import EventService
from src.Backend.services.analytics_service import AnalyticsService


class SimulationService:

    @staticmethod
    def tick():

        TrafficManager.reset()

        robots = FleetService.get_all_robots()

        for robot in robots:

            if FailureService.check(robot):
                continue

            # ---------------------------------
            # Robot is currently working
            # ---------------------------------

            if robot.status == "Working":

                print(f"Route       : {robot.route}")
                print(f"Route Index : {robot.route_index}")
                print(f"Route Length: {len(robot.route)}")

                print(f"\n========== {robot.robot_id} ==========")
                print(f"Before Move : {robot.location}")

                if robot.route_index < len(robot.route) - 1:

                    next_location = robot.route[
                        robot.route_index + 1
                    ]

                    if TrafficManager.can_move(next_location):

                        robot.route_index += 1
                        robot.location = next_location
                        AnalyticsService.add_distance()

                        EventService.log(
                            "Robot Moved",
                            robot.robot_id,
                            f"Moved to {next_location}"
                        )

                        print(
                            f"{robot.robot_id} moved to {next_location}"
                        )

                    else:

                        print(
                            f"{robot.robot_id} waiting. "
                            f"{next_location} is occupied."
                        )

                print(f"After Move  : {robot.location}")

                # Battery drain
                robot.battery -= random.randint(1, 5)

                # Temperature increase
                robot.temperature += round(
                    random.uniform(0.1, 0.8),
                    2
                )

                # Progress
                robot.task_progress += int(
                    100 / robot.estimated_ticks
                )

                if robot.task_progress > 100:
                    robot.task_progress = 100

                print(
                    f"Progress    : {robot.task_progress}%"
                )

                # -------------------------
                # Task Completed
                # -------------------------

                if robot.task_progress >= 100:

                    EventService.log(
                        "Task Completed",
                        robot.robot_id,
                        robot.task
                    )

                    AnalyticsService.increment(
                        "tasks_completed"
                    )

                    robot.route = []
                    robot.route_index = 0

                    print(
                        f"{robot.robot_id} completed task"
                    )

                    robot.status = "Idle"
                    robot.task = "Waiting"
                    robot.destination = "-"
                    robot.task_progress = 0

                # -------------------------
                # Battery Critical
                # -------------------------

                if robot.battery <= 15:

                    EventService.log(
                        "Battery Critical",
                        robot.robot_id,
                        f"{robot.battery}%"
                    )

                    print(
                        f"{robot.robot_id} battery critical"
                    )

                    robot.status = "Charging"
                    robot.task = "Charging"
                    robot.destination = "Charging Station"
                    robot.task_progress = 0

            # ---------------------------------
            # Charging
            # ---------------------------------

            elif robot.status == "Charging":

                robot.battery += 4

                if robot.battery >= 95:

                    EventService.log(
                        "Charging Complete",
                        robot.robot_id,
                        "Battery Fully Charged"
                    )

                    robot.battery = 100
                    robot.status = "Idle"
                    robot.task = "Waiting"
                    robot.destination = "-"
                    robot.temperature = 30
                    robot.task_progress = 0

            # ---------------------------------
            # Idle Robot
            # ---------------------------------

            elif robot.status == "Idle":

                task = TaskQueueService.pop()

                if task:

                    robot.status = "Working"
                    robot.task = task.task_name
                    robot.destination = task.destination
                    robot.task_progress = 0
                    robot.estimated_ticks = 5

                    EventService.log(
                        "Task Started",
                        robot.robot_id,
                        task.task_name
                    )

                    print(
                        f"{robot.robot_id} picked queued task -> {task.task_name}"
                    )

        return robots