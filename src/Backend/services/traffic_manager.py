class TrafficManager:

    reserved_locations = set()

    @staticmethod
    def reset():

        TrafficManager.reserved_locations.clear()

    @staticmethod
    def can_move(next_location):

        if next_location in TrafficManager.reserved_locations:
            return False

        TrafficManager.reserved_locations.add(next_location)

        return True