import os

import google.generativeai as genai
from dotenv import load_dotenv

from src.Backend.prompts.fleet_report_prompt import SYSTEM_PROMPT
from src.Backend.services.dashboard_service import DashboardService

# Load .env
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


class AISupervisor:

    @staticmethod
    def generate():

        dashboard = DashboardService.summary()

        prompt = f"""
        {SYSTEM_PROMPT}

        Fleet Data:

        {dashboard}
        """

        try:
            model = genai.GenerativeModel("gemini-3.6-flash")

            response = model.generate_content(prompt)

            return {
                "success": True,
                "report": response.text
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            }