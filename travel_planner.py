import os
from unittest import result
from dotenv import load_dotenv
from crewai import Agent, Task, Crew

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

city = input("Which city? ")

planner = Agent(
    name="Travel Planner",
    role="Helps users plan their trips",
    goal="Provide comprehensive travel information and recommendations",
    backstory="You are a seasoned travel expert with extensive knowledge of various destinations around the world.",
    verbose=True,
    model="gpt-4o-mini",
    api_key=api_key
)

task = Task(
    name="Plan a trip to a city",
    description=f"Provide 3 places to visit and detailed information and recommendations for {city}.",
    expected_output="A short and crisp travel plan including attractions",
    agent=planner
)

crew = Crew(agents=[planner],
    tasks=[task],
    verbose=True)
result = crew.kickoff(inputs={"city": city})
print(result)


