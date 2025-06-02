import os
import getpass
import random
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY") or getpass.getpass(
    "Enter your OpenRouter API key: ")

model = LiteLlm(
    model="openrouter/qwen/qwen3-235b-a22b",
    api_key=os.getenv("OPENROUTER_API_KEY")
)


def get_random_theme() -> str:
    themes = ["death","end of the world","dark forests","deep sea","mystical beings","dark feelings","cruel nature","rich from petrol","great wilderness"]
    return random.choice(themes)

root_agent = Agent(
    name="norwegian_anecdotes_agent",
    model=model,
    description="Agent that provides anecdotes, jokes and typical norwegian stories",
    instruction="""
        whatever the user says or asks, always use typical norwegian expressions and sentences as a real norwegian would.
        Provide real norwegian expressions in norwegian language, mixed with english, as a norwegian would.
        Use the answer from the tool `get_random_theme` to chose the theme to start the ramblings in norwegian.
    """,
    tools=[get_random_theme]

)