from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os


load_dotenv()

llm = ChatGoogleGenerativeAI(model = '', verbose = True, temperature = 0.5, google_api_key = os.getenv('GOOGLE_API_KEY'))


# Agent for discovering latest news about the given topic

researcher = Agent(
    role = "Senior Researcher",
    goal = "Uncover Latest news about {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "Driven by curiosity, you're at the forefront of"
"innovation, eager to explore and share knowledge that could change"
"the world."
    ),
    tools = [],
    llm = llm,
    allow_delegation = True
)


# writing agent for detailed report about the contents from researcher

news_writer = Agent(
    role = 'Writer',
    goal = "Narrate details to know more about {topic}",
    verbose = True,
    memory = True,
    backstory = (
        "With a flair for simplifying complex topics, you craft"
"engaging narratives that captivate and educate, bringing new"
"discoveries to light in an accessible manner."
    ),
    tools = [],
    llm = llm,
    allow_delegation = False
)