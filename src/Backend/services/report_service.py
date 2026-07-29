import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


class ReportService:

    @staticmethod
    def generate(system_report):

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

        prompt = f"""
You are a Robotics Fleet Operations Expert.

Analyze this report.

{system_report}

Write:
- Overall Fleet Health
- Problems
- Recommendations
- Priority Actions
"""

        response = llm.invoke(prompt)

        return response.content