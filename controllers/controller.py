from flask import render_template, request
from app import app
from models.event import Event
from models.events import events_list, add_new_event

@app.route('/events')
def index():
    return render_template('index.html', events=events_list)

@app.route('/events/<int:index>')
def single_event(index):
    return render_template('event.html', event=events_list[index], index=index)

@app.route('/events', methods=['POST'])
def add_event():
    print(request.form)
    event_date = request.form['date']
    event_name = request.form['name']
    event_number_guest = int(request.form['number_of_guests'])
    event_room_location = request.form['room_location']
    event_description = request.form['description']
    # event_recurring_monthly = request.form['recurring_monthly']
    if 'recurring_monthly' in request.form:
        event_recurring_monthly = True
    else:
        event_recurring_monthly = False
    new_event = Event(date=event_date, name=event_name, number_guest=event_number_guest,
        room_location=event_room_location, description=event_description, recurring_monthly=event_recurring_monthly)
    add_new_event(new_event)
    return render_template('index.html', events=events_list)