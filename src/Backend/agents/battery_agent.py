from src.Backend.services.fleet_service import FleetService


class BatteryAgent:

    CRITICAL = 10
    LOW = 20

    @staticmethod
    def analyze():

        robots = FleetService.get_all_robots()

        low_battery = []

        for robot in robots:

            if robot.battery <= BatteryAgent.CRITICAL:

                level = "Critical"

            elif robot.battery <= BatteryAgent.LOW:

                level = "Low"

            else:
                continue

            low_battery.append(
                {
                    "robot_id": robot.robot_id,
                    "battery": robot.battery,
                    "level": level,
                    "location": robot.location,
                    "status": robot.status,
                    "recommendation": "Immediate Charging" if level == "Critical" else "Schedule Charging"
                }
            )

        return {
            "total_robots": len(robots),
            "low_battery_count": len(low_battery),
            "robots": low_battery
        }