from src.Backend.simulation.analytics import analytics


class AnalyticsService:

    @staticmethod
    def increment(metric):

        analytics[metric] += 1

    @staticmethod
    def add_distance():

        analytics["distance_travelled"] += 1

    @staticmethod
    def get():

        return analytics