from src.Backend.services.fleet_service import FleetService


class DecisionExecutor:

    @staticmethod
    def execute(actions):

        for action in actions:

            robot_id = action["robot"]
            command = action["command"]

            robot = FleetService.get_robot(robot_id)

            if robot is None:
                continue

            if command == "Charge":
                robot.status = "Charging"
                robot.task = "Charging Station"

            elif command == "ContinueMission":
                robot.status = "Working"

            elif command == "Idle":
                robot.status = "Idle"

        return FleetService.get_all_robots()