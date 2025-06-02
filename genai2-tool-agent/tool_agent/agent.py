from google.adk.agents import Agent
from google.adk.tools import google_search

def get_current_time() -> dict:
    from datetime import datetime
    """
    Gets the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash",
    description="A tool agent that can perform various tasks using tools.",
    instruction="""
You are a tool agent. You can perform various tasks using tools:
- google_search: Search the web for information.
    """,
    #tools=[get_current_time],
    tools=[google_search],
)   