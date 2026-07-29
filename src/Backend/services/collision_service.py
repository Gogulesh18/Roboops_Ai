from src.Backend.services.fleet_service import FleetService
from src.Backend.services.analytics_service import AnalyticsService


class CollisionService:

    @staticmethod
    def detect():

        robots = FleetService.get_all_robots()

        locations = {}

        collisions = []

        print("\n===== COLLISION CHECK =====")

        for robot in robots:

            print(
                robot.robot_id,
                robot.location,
                robot.status
            )

            if robot.status != "Working":
                continue

            if robot.location in locations:

                print(
                    f"Collision Found at {robot.location}"
                )
                AnalyticsService.increment(
                    "collisions"
                )
                collisions.append(
                    {
                        "location": robot.location,
                        "robots": [
                            locations[robot.location],
                            robot.robot_id
                        ]
                    }
                )

            else:

                locations[robot.location] = robot.robot_id

        print(collisions)

        return collisions