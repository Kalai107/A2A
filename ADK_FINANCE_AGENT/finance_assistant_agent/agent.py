from google.adk.agents import LlmAgent
from google.adk.tools import google_search

finance_assistance_agent=LlmAgent(
    name="finance_assistance_agent",
    model="gemini-2.5-flash",
    description="A simple finance assistant that helps with user finance goals.",
    instruction="""you are a friendly finance assistant.
        you can help answer user's generic questions on finance and help plan 
        thier finance goals and be more friendly and positive
    """,
    tools=[google_search]
)

root_agent=finance_assistance_agent