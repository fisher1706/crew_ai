from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv

from calculator_tool import CalculateTool


load_dotenv()

math_input = "2 * 9 / 4"  # Default math equation

calculate = CalculateTool()


math_agent = Agent(
    role="Math Magician",
    goal="You are able to evaluate any math expression",
    backstory="YOU ARE A MATH WHIZ.",
    tools=[calculate],
    verbose=True
)



writer = Agent(
    role="Writer",
    goal="Craft compelling explanations based from results of math equations.",
    backstory="""You are a renowned Content Strategist, known for your insightful and engaging articles.  
    You transform complex concepts into compelling narratives.
    """,
    verbose=True
)


task1 = Task(
    description=f"{math_input}",
    expected_output="Give full details in bullet points.",
    agent=math_agent
)


task2 = Task(
    description="""using the insights provided, explain in great detail how the equation and result were formed.""",
    expected_output="""Explain in great detail and save in markdown.  Do no add the triple tick marks at the 
                    beginning or end of the file.  Also don't say what type it is in the first line.""",
    output_file="markdown/math.md",
    agent=writer
)


crew = Crew(
    agents=[math_agent, writer],
    tasks=[task1, task2],
    process=Process.sequential,
    verbose=True
)


result = crew.kickoff()


if __name__ == '__main__':
    print(result)
