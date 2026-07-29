from src.Backend.simulation.warehouse_map import warehouse
import random


class NavigationService:

    @staticmethod
    def move(robot):

        current = robot.location

        if current not in warehouse:
            return

        neighbours = warehouse[current]

        if neighbours:
            robot.location = random.choice(neighbours)