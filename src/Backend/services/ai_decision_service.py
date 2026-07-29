import json
import os

import google.generativeai as genai
from dotenv import load_dotenv

from src.Backend.prompts.action_prompt import SYSTEM_PROMPT
from src.Backend.services.dashboard_service import DashboardService
from src.Backend.services.decision_executor import DecisionExecutor

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


class AIDecisionService:

    @staticmethod
    def decide():

        dashboard = DashboardService.summary()

        prompt = f"""
{SYSTEM_PROMPT}

Fleet Data:

{dashboard}
"""

        model = genai.GenerativeModel("gemini-3.6-flash")

        response = model.generate_content(prompt)

        text = response.text.strip()

        # Remove markdown if Gemini wraps JSON in ```json
        text = text.replace("```json", "").replace("```", "").strip()

        decision = json.loads(text)

        DecisionExecutor.execute(
            decision["actions"]
        )

        return decision