"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Join the school soccer team and compete in matches",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 22,
        "participants": ["alex@mergington.edu", "james@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Practice basketball skills and participate in tournaments",
        "schedule": "Wednesdays and Fridays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["luke@mergington.edu", "matthew@mergington.edu"]
    },
    "Art Club": {
        "description": "Explore various art techniques and create your own masterpieces",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Drama Club": {
        "description": "Learn acting skills and perform in school plays",
        "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["isabella@mergington.edu", "amelia@mergington.edu"]
    },
    "Math Club": {
        "description": "Solve challenging math problems and prepare for competitions",
        "schedule": "Tuesdays, 3:30 PM - 4:30 PM",
        "max_participants": 10,
        "participants": ["ethan@mergington.edu", "noah@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific concepts",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["liam@mergington.edu", "elijah@mergington.edu"]
    }
}


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specificy activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")
    # Validate max participants
    if len(activity["participants"]) >= activity["max_participants"]:
        raise HTTPException(status_code=400, detail="Activity is full")
    # Validate email format
    if "@" not in email or "." not in email.split("@")[-1]:
        raise HTTPException(status_code=400, detail="Invalid email format")
    # Validate email domain
    if not email.endswith("@mergington.edu"):
        raise HTTPException(status_code=400, detail="Email must be from mergington.edu")
    # Validate email is not empty
    if not email:
        raise HTTPException(status_code=400, detail="Email cannot be empty")
    # Validate email is not too long
    if len(email) > 50:
        raise HTTPException(status_code=400, detail="Email is too long")
    # Validate email is not too short
    if len(email) < 5:
        raise HTTPException(status_code=400, detail="Email is too short")
    # Validate email is not a duplicate
    for activity in activities.values():
        if email in activity["participants"]:
            raise HTTPException(status_code=400, detail="Email is already signed up for another activity")        
        
    # Validate email is not a teacher
    if email.startswith("teacher@"):
        raise HTTPException(status_code=400, detail="Teachers cannot sign up for activities")
    # Validate email is not a staff
    if email.startswith("staff@"):
        raise HTTPException(status_code=400, detail="Staff cannot sign up for activities")
    # Validate email is not a parent
    if email.startswith("parent@"):
        raise HTTPException(status_code=400, detail="Parents cannot sign up for activities")
    # Validate email is not a guardian
    if email.startswith("guardian@"):
        raise HTTPException(status_code=400, detail="Guardians cannot sign up for activities")
    # Validate email is not a student
    if email.startswith("student@"):
        raise HTTPException(status_code=400, detail="Students cannot sign up for activities")
    # Validate email is not a alumni
    if email.startswith("alumni@"):
        raise HTTPException(status_code=400, detail="Alumni cannot sign up for activities")
    # Validate email is not a volunteer
    if email.startswith("volunteer@"):
        raise HTTPException(status_code=400, detail="Volunteers cannot sign up for activities")
    # Validate email is not a guest
    if email.startswith("guest@"):
        raise HTTPException(status_code=400, detail="Guests cannot sign up for activities")
    # Validate email is not a visitor
    if email.startswith("visitor@"):
        raise HTTPException(status_code=400, detail="Visitors cannot sign up for activities")
    # Validate email is not a contractor
    if email.startswith("contractor@"):
        raise HTTPException(status_code=400, detail="Contractors cannot sign up for activities")
    # Validate email is not a vendor
    if email.startswith("vendor@"):
        raise HTTPException(status_code=400, detail="Vendors cannot sign up for activities")
    # Validate email is not a supplier
    if email.startswith("supplier@"):
        raise HTTPException(status_code=400, detail="Suppliers cannot sign up for activities")
    # Validate email is not a partner
    if email.startswith("partner@"):
        raise HTTPException(status_code=400, detail="Partners cannot sign up for activities")
    # Validate email is not a sponsor
    if email.startswith("sponsor@"):
        raise HTTPException(status_code=400, detail="Sponsors cannot sign up for activities")
    # Validate email is not a donor
    if email.startswith("donor@"):
        raise HTTPException(status_code=400, detail="Donors cannot sign up for activities")
    

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
