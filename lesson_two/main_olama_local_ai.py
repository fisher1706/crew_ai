import os
from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI


# set key for local llm
os.environ["OPENAI_API_KEY"] = "sk-proj-1111"


# install ollama local before run
llm = ChatOpenAI(
    model="phi3:3.8b",
    base_url="http://localhost:11434/v1"
)


info_agent = Agent(
    role="Information Agent",
    goal="Give compelling information about a certain topic",
    backstory="""
        You love to know information.  People love and hate you for it.  You win most of the
        quizzes at your local pub.
    """,
    llm=llm
)


task = Task(
    description="Tell me all about the box jellyfish.",
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
    print(result)
