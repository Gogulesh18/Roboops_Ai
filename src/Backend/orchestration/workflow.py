from langgraph.graph import StateGraph, END

from src.Backend.orchestration.state import FleetState

from src.Backend.agents.battery_agent import BatteryAgent
from src.Backend.agents.traffic_agent import TrafficAgent
from src.Backend.agents.maintenance_agent import MaintenanceAgent

def battery_node(state):

    state["battery"] = BatteryAgent.analyze()

    return state


def traffic_node(state):

    state["traffic"] = TrafficAgent.analyze()

    return state


def maintenance_node(state):

    state["maintenance"] = MaintenanceAgent.analyze()

    return state

builder = StateGraph(FleetState)

builder.add_node("battery", battery_node)

builder.add_node("traffic", traffic_node)

builder.add_node("maintenance", maintenance_node)

builder.set_entry_point("battery")

builder.add_edge("battery", "traffic")

builder.add_edge("traffic", "maintenance")

builder.add_edge("maintenance", END)

graph = builder.compile()