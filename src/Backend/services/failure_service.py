import uuid

from src.Backend.models.task import Task
from src.Backend.services.event_service import EventService
from src.Backend.services.task_queue_service import TaskQueueService
from src.Backend.services.analytics_service import AnalyticsService


class FailureService:

    BATTERY_THRESHOLD = 10
    TEMPERATURE_THRESHOLD = 80

    @staticmethod
    def check(robot):

        if robot.status == "Charging":
            return False
       
        # Low Battery
        if robot.battery <= FailureService.BATTERY_THRESHOLD:
            return FailureService.fail(
                robot,
                "Low Battery"
            )

        # High Temperature
        if robot.temperature >= FailureService.TEMPERATURE_THRESHOLD:
            return FailureService.fail(
                robot,
                "High Temperature"
            )

        return False

    @staticmethod
    def fail(robot, reason):

        print(f"{robot.robot_id} FAILED : {reason}")

        # ✅ Log Failure Event
        EventService.log(
            "Failure",
            robot.robot_id,
            reason
        )
        AnalyticsService.increment(
            "failures"
        )

        # Save unfinished task
        if robot.task != "Waiting":

            TaskQueueService.add(
                Task(
                    task_id=str(uuid.uuid4()),
                    task_name=robot.task,
                    priority="Normal",
                    destination=robot.destination,
                    status="Waiting"
                )
            )

            # ✅ Log Task Requeued
            EventService.log(
                "Task Requeued",
                robot.robot_id,
                robot.task
            )

        robot.status = "Charging"
        robot.destination = "Charging Station"
        robot.task = "Charging"

        robot.route = []
        robot.route_index = 0
        robot.task_progress = 0

        return True