# from crew import initiliaze_crew_ai
# import json
# from pprint import pprint
# from IPython.display import Markdown


# event_details = {
#     'event_topic': "Tech Innovation Conference",
#     'event_description': "A gathering of tech innovators "
#                          "and industry leaders "
#                          "to explore future technologies.",
#     'event_city': "San Francisco",
#     'tentative_date': "2024-09-15",
#     'expected_participants': 500,
#     'budget': 20000,
#     'venue_type': "Conference Hall"
# }
# event_management_crew = initiliaze_crew_ai()
# result = event_management_crew.kickoff(inputs=event_details)

# with open('venue_details.json') as f:
#    data = json.load(f)

# pprint(data)
# Markdown("marketing_report.md")

import streamlit as st
import json
from pprint import pprint
from crew import initiliaze_crew_ai

# Streamlit App Title
st.title("Event Planner")

# Sidebar for Input Fields
st.sidebar.header("Enter Event Details")

# Input Fields
event_topic = st.sidebar.text_input("Event Topic", "Tech Innovation Conference")
event_description = st.sidebar.text_area(
    "Event Description",
    "A gathering of tech innovators and industry leaders to explore future technologies."
)
event_city = st.sidebar.text_input("Event City", "San Francisco")
tentative_date = st.sidebar.date_input("Tentative Date")
expected_participants = st.sidebar.number_input("Expected Participants", min_value=1, value=500, step=1)
budget = st.sidebar.number_input("Budget (in USD)", min_value=0, value=20000, step=100)
venue_type = st.sidebar.selectbox("Venue Type", ["Conference Hall", "Outdoor", "Banquet", "Auditorium"])

# Submit Button
if st.sidebar.button("Plan Event"):
    # Organizing Inputs
    event_details = {
        'event_topic': event_topic,
        'event_description': event_description,
        'event_city': event_city,
        'tentative_date': str(tentative_date),
        'expected_participants': expected_participants,
        'budget': budget,
        'venue_type': venue_type,
    }

    # Initialize Crew AI and Process the Event
    event_management_crew = initiliaze_crew_ai()
    result = event_management_crew.kickoff(inputs=event_details)

    try:
    # Load the JSON file
        with open('venue_details.json') as f:
            venue_data = json.load(f)

        # Display Venue Details Section
        st.header("Venue Details")
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Name:**")
            st.markdown(f"🏢{venue_data['name']}")
            st.write("**Address:**")
            st.markdown(f"📍{venue_data['address']}")


        with col2:
            st.write("**Capacity:**")
            st.markdown(f"👥 {venue_data['capacity']}")
            st.write("**Booking Status:**")
            st.markdown(f"📅  {venue_data['booking_status']}")



    except FileNotFoundError:
        st.warning("No venue details file found.")
        
    
    try:
    # Load the JSON file
        # Load the JSON data (ensure you have the equipment.json file in the same directory)
        with open("equipment.json", "r") as file:
            equipment_data = json.load(file)
        st.header("Equipment Details")
        # Create two columns for displaying the data
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Catering Name:**")
            st.markdown(f"🏢 {equipment_data['catering_name']}")
            st.write("**Catering Address:**")
            st.markdown(f"📍 {equipment_data['catering_address']}")

        with col2:
            st.write("**Equipment Name:**")
            st.markdown(f"⚙️ {equipment_data['equipment_name']}")
            st.write("**Booking Status:**")
            st.markdown(f"📅 {equipment_data['booking_status']}")



    except FileNotFoundError:
        st.warning("No venue details file found.")


    # Markdown Report (if available)
    try:
        with open("marketing_report.md", "r") as md_file:
            markdown_content = md_file.read()
        st.header("Marketing Report")
        st.markdown(markdown_content)
    except FileNotFoundError:
        st.warning("No marketing report file found.")
