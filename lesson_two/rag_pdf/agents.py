from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from crewai_tools import PDFSearchTool
from dotenv import load_dotenv


load_dotenv(verbose=True)


class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7
        )
        self.OpenAIGPT4 = ChatOpenAI(
            model="gpt-4",
            temperature=0.7
        )


    def pdf_agent(self) -> Agent:

        pdf_tool = PDFSearchTool(pdf_path="gpt-4-analysis.pdf")

        return Agent(
            role="Senior PDF Analyst",
            backstory=dedent("""
                You can find anything in a pdf.  The people need you.
            """),
            goal=dedent(f"""
                Uncover any information from pdf files exceptionally well.
            """),
            tools=[pdf_tool],
            llm=self.OpenAIGPT4,
            verbose=True
        )


    def writer_agent(self) -> Agent:
        return Agent(
            role="Writer",
            backstory=dedent("""
                You are a technical writer that crafts clear and concise documents.
                You excel at transforming complex information into easily understandable content.
            """),
            goal=dedent("""
                Create well-structured and informative documents based on provided data and insights.
            """),
            llm=self.OpenAIGPT35,
            verbose=True
        )