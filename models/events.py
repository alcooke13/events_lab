from models.event import Event
from datetime import datetime

event1 = Event(datetime(2022, 11, 3, 15, 30, 17), "Class Meeting", 23, "Classroom", "Meeting 59", True)
event2 = Event(datetime(2022, 11, 4, 18, 30, 27), "Hangouts", 32, "The Pub", "Meet everyone", False)

events_list = [event1, event2]

def add_new_event(new_event):
    events_list.append(new_event)