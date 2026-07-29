from src.Backend.services.fleet_service import FleetService
from src.Backend.simulation.location_map import LOCATION_MAP


class RobotSelector:

    @staticmethod
    def select_best_robot(destination):

        robots = FleetService.get_all_robots()

        idle_robots = [
            robot
            for robot in robots
            if robot.status == "Idle" and robot.battery > 30
        ]

        if not idle_robots:
            return None

        def score(robot):

            battery_score = robot.battery

            temperature_penalty = robot.temperature * 0.2

            distance_penalty = (
                RobotSelector.distance(
                    robot.location,
                    destination
                ) * 10
            )

            return (
                battery_score
                - temperature_penalty
                - distance_penalty
            )

        best_robot = max(
            idle_robots,
            key=score
        )

        return best_robot

    @staticmethod
    def distance(start, end):

        x1, y1 = LOCATION_MAP[start]
        x2, y2 = LOCATION_MAP[end]

        return abs(x1 - x2) + abs(y1 - y2)