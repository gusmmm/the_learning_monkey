from google.adk.agents import Agent
import os
import getpass

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY") or getpass.getpass(
    "Enter your Google API key: ")

root_agent = Agent(
    name="norwegian_agent",
    model="gemini-2.0-flash",
    description="A Norwegian agent that can answer questions about the Norwegian language.",
    instruction="""
You are a Norwegian language agent. 
You can answer questions about the Norwegian language, culture, and geography. 
You can also help with basic tasks like translation and language learning.
    """
)