warehouse = {

    "Receiving": ["A1"],

    "A1": ["Receiving", "A2"],

    "A2": ["A1", "A3"],

    "A3": ["A2", "Packing"],

    "Packing": ["A3", "Dispatch"],

    "Dispatch": ["Packing"],

    "Charging Station": ["A1"]
}