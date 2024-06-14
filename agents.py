from crewai import Agent
from tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain_community.tools import DuckDuckGoSearchRun


search_tool = DuckDuckGoSearchRun()


load_dotenv()

llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash', verbose = True, temperature = 0.5, google_api_key = os.getenv('GOOGLE_API_KEY'))


# Agent for discovering latest news about the given topic

researcher = Agent(
    role = "Senior Research Analyst",
    goal = "Uncover cuttting edge development in {topic}",
    backstory = """You work at a leading tech think tank
    your expertise lies in identifying emergin trends.
    you have a knack for dissecting complex data and presenting actionable insights """,
    verbose = True,
    allow_delegation = True,
    tools = [tool],
    llm = llm
)



# writing agent for detailed report about the contents from researcher

writer = Agent(
    role = "Tech Content Strategist",
    goal = "Craft compelling content on {topic}",
    backstory = """You are a renowed content strategist known for your insightful and engaging articles.
     you transform complex concepts into compelling narratives """,
     verbose = True,
     allow_delegation = True,
     llm = llm
)