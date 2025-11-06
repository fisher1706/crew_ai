from dotenv import load_dotenv
from crewai import Crew

from tasks import MeetingPrepTask
from agents import MeetingPrepAgents


def main():
    load_dotenv()

    print("Welcome to the Meeting Prep Crew")
    print("-" * 200)

    meeting_participants = input("What are the emails for the meeting participants (comma separated)? \n")
    meeting_context = input("What is the context for the meeting? \n")
    meeting_objectives = input("What are the objectives for the meeting? \n")

    task = MeetingPrepTask()
    agents = MeetingPrepAgents()

    # create agents
    research_agent = agents.research_agent()
    industry_analist_agent = agents.industry_analist_agent()
    meeting_strategist_agent = agents.meeting_strategist_agent()
    summary_and_briefing_agent = agents.summary_and_briefing_agent()

    # create tasks
    research_task = task.research_task(
        agent=research_agent,
        participants=meeting_participants,
        meeting_context= meeting_context
    )

    industry_analist_task = task.industry_analist_task(
        agent=industry_analist_agent,
        industry=meeting_participants,
        meeting_context=meeting_context
    )

    meeting_strategy_task = task.meeting_strategy_task(
        agent=meeting_strategist_agent,
        meeting_context=meeting_context,
        research_objective=meeting_objectives
    )

    summary_and_briefing_task = task.summary_and_briefing_task(
        agent=summary_and_briefing_agent,
        meeting_context=meeting_context,
        research_objective=meeting_objectives
    )

    meeting_strategy_task.context = [research_task, industry_analist_task]
    summary_and_briefing_task.context = [research_task, industry_analist_task, meeting_strategy_task]

    crew = Crew(
        agents=[
            research_agent,
            industry_analist_agent,
            meeting_strategist_agent,
            summary_and_briefing_agent
        ],

        tasks=[
            research_task,
            industry_analist_task,
            meeting_strategy_task,
            summary_and_briefing_task
        ]
    )

    result = crew.kickoff()
    print(result)









if __name__ == '__main__':
    main()