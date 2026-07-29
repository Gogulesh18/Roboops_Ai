from src.Backend.models.robot import Robot

fleet = [

    Robot(
        robot_id="R001",
        battery=8,
        location="A1",
        status="Working",
        task="Picking",
        destination="Dispatch",
        speed=1.2,
        temperature=34.5
    ),

    Robot(
        robot_id="R002",
        battery=41,
        location="A4",
        status="Working",
        task="Waiting",
        destination="-",
        speed=0.9,
        temperature=37.8
    ),

    Robot(
        robot_id="R003",
        battery=17,
        location="Charging Station",
        status="Charging",
        task="Charging",
        destination="Dock",
        speed=0,
        temperature=30.4
    ),

]