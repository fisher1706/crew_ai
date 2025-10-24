from textwrap import dedent
from crewai import Agent

from tools import ExaSearchTool


class MeetingPrepAgents:
    @staticmethod
    def research_agent():
        return Agent(
            role='Research Specialist',
            goal='Conduct thorough research on people and companies involved in the meeting',
            tools=ExaSearchTool().tools(),
            backstory=dedent("""\
                As a Research Specialist, your mission is to uncover detailed information
                about the individuals and entities participating in the meeting. Your insights
                will lay the groundwork for strategic meeting preparation."""),
            verbose=True
        )

    @staticmethod
    def industry_analist_agent():
        return Agent(
            role='Industry Analyst',
            goal='Analyze current trends and challenges in the relevant industry',
            tools=ExaSearchTool().tools(),
            backstory=dedent("""\
                As an Industry Analyst, you are tasked with providing a deep understanding
                of the industry landscape. Your analysis will help inform strategies and
                decisions for the upcoming meeting."""),
            verbose=True
        )

    @staticmethod
    def meeting_strategist_agent():
        return Agent(
            role='Meeting Strategist',
            goal='Develop a strategic plan for the meeting based on research and analysis',
            backstory=dedent("""\
                As a Meeting Strategist, your role is to synthesize research findings
                and industry insights into a coherent strategy. Your plan will guide
                the discussion and objectives of the meeting."""),
            verbose=True
        )

    @staticmethod
    def summary_and_briefing_agent():
        return Agent(
            role='Summary and Briefing Specialist',
            goal='Compile research and analysis into a concise briefing document',
            backstory=dedent("""\
                As a Summary and Briefing Specialist, your task is to distill complex
                information into clear, actionable insights. Your briefing will ensure
                all meeting participants are well-informed and prepared."""),
            verbose=True
        )
