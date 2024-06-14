from crewai import Task
from tools import tool
from agents import researcher,news_writer

# Research task
task1 = Task(
description="Conduct a comprehensive analysis of the latest advancements in AI in 2024. Identify key trends, breakthrough technologies, and potential industry impacts. Your final answer MUST be a full analysis report",
agent = researcher,
expected_output='A comprehensive 5 paragraphs long report on the latest trends.',
)

# Writing task with language model configuration
task2 = Task(
description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
Identify key trends, breakthrough technologies, and potential industry impacts.
Your final answer MUST be a full analysis report""",
agent = researcher,
expected_output = "A final blog in html format"
)