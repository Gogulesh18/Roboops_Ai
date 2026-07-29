from src.Backend.orchestration.workflow import graph


class CoordinatorAgent:

    @staticmethod
    def run():

        result = graph.invoke(
            {
                "battery": {},
                "traffic": {},
                "maintenance": {}
            }
        )

        return {
            "system": "RoboOps AI",
            "fleet_status": result
        }