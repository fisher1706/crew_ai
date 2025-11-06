from dotenv import load_dotenv
import os
from crewai import Agent, Task, Crew


load_dotenv()


info_agent = Agent(
    role="Information Agent",
    goal="Giv compelling information about certain topics",
    backstory="""
        You love to know information.  
        People love and hate you for it.  
        You win most of the quizzes at your local pub.
        """
)

task = Task(
    description="Tell me all about the blue-ringed octopus.",
    expected_output="Give me a quick summary and then also give me 7 bullet points describing it.",
    agent=info_agent
)


crew = Crew(
    agents=[info_agent],
    tasks=[task],
    verbose=True
)


result = crew.kickoff()


if __name__ == '__main__':
    model = os.getenv("OPEN_AI_MODEL")
    key = os.getenv("OPENAI_API_KEY")

    print(model)
    print(key)

    print(result)