from src.Backend.services.fleet_service import FleetService


class TrafficAgent:

    @staticmethod
    def analyze():

        robots = FleetService.get_all_robots()

        congestion = {}

        for robot in robots:

            zone = robot.location

            congestion[zone] = congestion.get(zone, 0) + 1

        busy = []

        for zone, count in congestion.items():

            if count >= 2:

                busy.append(
                    {
                        "zone": zone,
                        "robots": count,
                        "recommendation": "Redistribute robots"
                    }
                )

        return {
            "zones": congestion,
            "congested": busy
        }