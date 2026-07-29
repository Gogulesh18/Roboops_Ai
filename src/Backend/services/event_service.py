from datetime import datetime
from src.Backend.simulation.event_log import event_log


class EventService:

    @staticmethod
    def log(event_type, robot_id, message):

        event_log.append(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "event": event_type,
                "robot": robot_id,
                "message": message
            }
        )

    @staticmethod
    def get_all():

        return event_log