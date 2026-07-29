import threading
import time

from src.Backend.services.ai_decision_service import AIDecisionService
from src.Backend.services.decision_executor import DecisionExecutor


class AutoPilotService:

    running = False

    @staticmethod
    def start():

        if AutoPilotService.running:
            return

        AutoPilotService.running = True

        thread = threading.Thread(
            target=AutoPilotService.loop,
            daemon=True
        )

        thread.start()

    @staticmethod
    def loop():

        while AutoPilotService.running:

            try:

                decision = AIDecisionService.decide()

                print("Decision:", decision)

                DecisionExecutor.execute(decision["actions"])

                print("🤖 AI Autopilot executed")

            except Exception as e:

                print(e)

            time.sleep(60)

    @staticmethod
    def stop():

        AutoPilotService.running = False