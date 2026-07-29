from src.Backend.simulation.fleet import fleet
from src.Backend.models.robot import Robot


class FleetService:

    @staticmethod
    def get_all_robots():
        return fleet

    @staticmethod
    def get_robot(robot_id: str):
        for robot in fleet:
            if robot.robot_id == robot_id:
                return robot
        return None

    @staticmethod
    def add_robot(robot: Robot):
        fleet.append(robot)
        return robot