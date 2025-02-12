from crewai import Agent, Crew, Task
from agents import venue_coordinator,logistics_manager,marketing_communications_agent
from Tasks import venue_task,logistics_task,marketing_task

# Define the crew with agents and tasks

def initiliaze_crew_ai():
    event_management_crew = Crew(
        agents=[venue_coordinator, 
                logistics_manager,marketing_communications_agent],
        
        tasks=[venue_task, 
            logistics_task,marketing_task],
        
        verbose=True
    )
    return event_management_crew