import os
from textwrap import dedent

from crewai import Crew
from decouple import config

from agents import CustomAgents
from tasks import CustomTasks


os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")


class CustomCrew:
    def __init__(self, var):
        self.var = var


    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()


        # Define your custom agents and tasks here
        pdf_agent = agents.pdf_agent()
        writer_agent = agents.writer_agent()


        # Custom tasks include agent name and variables as input
        task_one = tasks.pdf_task(
            agent=pdf_agent,
            var=self.var
        )

        tsk_two = tasks.writer_task(
            agent=writer_agent
        )


        # Define your custom crew here
        crew = Crew(
            agents=[
                pdf_agent,
                writer_agent
            ],
            tasks=[
                task_one,
                tsk_two
            ],
            verbose=True
        )


        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")
    var1 = input(dedent("""Enter variable 1: """))

    custom_crew = CustomCrew(var1)
    result_out = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result_out)

