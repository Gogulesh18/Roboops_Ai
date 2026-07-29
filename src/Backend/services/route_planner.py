class RoutePlanner:

    ROUTES = {

        ("Receiving", "Dispatch"):
            ["Receiving", "A1", "A2", "A3", "Packing", "Dispatch"],

        ("A1", "Dispatch"):
            ["A1", "A2", "A3", "Packing", "Dispatch"],

        ("A2", "Dispatch"):
            ["A2", "A3", "Packing", "Dispatch"],

        ("A3", "Dispatch"):
            ["A3", "Packing", "Dispatch"],

        ("Packing", "Dispatch"):
            ["Packing", "Dispatch"]
    }

    @staticmethod
    def calculate(start, destination):

        return RoutePlanner.ROUTES.get(
            (start, destination),
            [start]
        )