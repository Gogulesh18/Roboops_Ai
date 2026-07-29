from src.Backend.services.fleet_service import FleetService


class HealthService:

    @staticmethod
    def calculate():

        robots = FleetService.get_all_robots()

        score = 100

        for robot in robots:

            if robot.battery < 20:
                score -= 10

            if robot.temperature > 45:
                score -= 15

            if robot.status == "Charging":
                score -= 2

        return {
            "fleet_health_score": max(score, 0)
        }