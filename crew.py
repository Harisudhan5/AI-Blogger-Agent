from crewai import Crew,Process
from tasks import task1,task2
from agents import researcher,writer

## Forming the tech focused crew with some enhanced configuration
crew = Crew(
    agents = [researcher,writer],
    tasks = [task1,task2],
    verbose=2
)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)