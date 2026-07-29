from src.Backend.services.fleet_service import FleetService


class MaintenanceAgent:

    @staticmethod
    def analyze():

        robots = FleetService.get_all_robots()

        maintenance_required = []

        for robot in robots:

            if robot.battery < 30 and robot.status == "Working":

                maintenance_required.append(
                    {
                        "robot_id": robot.robot_id,
                        "issue": "Battery degradation risk",
                        "recommendation": "Schedule preventive maintenance"
                    }
                )

        return {
            "count": len(maintenance_required),
            "robots": maintenance_required
        }