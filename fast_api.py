from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crew import initiliaze_crew_ai
from datetime import date
import json

# FastAPI App Initialization
app = FastAPI(title="Event Planner API")

class event_details(BaseModel):
    event_topic: str
    event_description: str
    event_city: str
    tentative_date: date
    expected_participants: int
    budget: int
    venue_type: str

# Root Endpoint
@app.get("/", response_model=dict)
def Home():
    return {"message": "Welcome to Event Planner"}

# Endpoint for Event Planning
@app.post("/plan-event/", response_model=dict)
def plan_event(event_details: event_details):
    # Organize Inputs
    event_data = event_details.model_dump()

    # Initialize Crew AI and Process the Event
    event_management_crew = initiliaze_crew_ai()
    result = event_management_crew.kickoff(inputs=event_data)

    # Return Event Details and Results
    return {
        "event_details": event_data,
        "crew_ai_output": result
    }
    

# Endpoint to Load Venue Details (Mocked JSON File)
@app.get("/venue-details/", response_model=dict)
def get_venue_details():
    try:
        with open("venue_details.json") as f:
            venue_data = json.load(f)
        return venue_data
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Venue details file not found.")

# Endpoint to Load Marketing Report (Markdown File)
@app.get("/marketing-report/", response_model=dict)
def get_marketing_report():
    try:
        with open("marketing_report.md", "r") as md_file:
            markdown_content = md_file.read()
        return {"report": markdown_content}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Marketing report file not found.")
    
    
