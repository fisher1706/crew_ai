from textwrap import dedent
from crewai import Task


class MeetingPrepTask:
    @staticmethod
    def research_task(agent, participants: str, meeting_context: str):
        """Creates a research task for meeting preparation."""
        return Task(
            description=dedent(f"""
                Conduct comprehensive research on each of the individuals and companies
                involved in the upcoming meeting. Gather information on recent
                news, achievements, professional background, and any relevant
                business activities.

                Participants: {participants}
                Meeting Context: {meeting_context}
            """),
            expected_output=dedent("""
                A detailed report summarizing key findings about each participant
                and company, highlighting information that could be relevant for the meeting.
            """),
            async_execution=True,
            agent=agent
        )

    @staticmethod
    def industry_analist_task(agent, industry, meeting_context):
        return Task(
            description=dedent(f"""\
              Analyze the current trends, challenges, and opportunities within the
              {industry} industry. Provide insights that could be pertinent to the
              upcoming meeting.

              Industry: {industry}
              Meeting Context: {meeting_context}"""),

            expected_output=dedent("""\
              A comprehensive analysis report detailing the latest trends,
              challenges, and opportunities in the specified industry."""),

            async_execution=True,

            agent=agent
        )


    @staticmethod
    def meeting_strategy_task(agent, meeting_context, research_report, industry_analysis):
        return Task(
            description=dedent(f"""\
              Develop a strategic plan for the upcoming meeting based on the
              research report and industry analysis. Identify key points to
              address, potential questions to ask, and strategies to achieve
              desired outcomes.

              Meeting Context: {meeting_context}
              Research Report: {research_report}
              Industry Analysis: {industry_analysis}"""),

            expected_output=dedent("""\
              A strategic plan outlining key discussion points, questions,
              and strategies for the meeting."""),

            async_execution=True,

            agent=agent
        )


    @staticmethod
    def summary_and_briefing_task(agent, meeting_context, strategy_plan):
        return Task(
            description=dedent(f"""\
              Create a concise summary and briefing document for the meeting
              participants. This document should encapsulate the strategic plan,
              key insights from the research and industry analysis, and any
              essential information needed for the meeting.

              Meeting Context: {meeting_context}
              Strategy Plan: {strategy_plan}"""),

            expected_output=dedent("""\
              A well-structured summary and briefing document for meeting participants."""),

            async_execution=True,

            agent=agent
        )




if __name__ == '__main__':
    data = dedent("A well-structured summary and briefing document for meeting participants.")
    print(data)
