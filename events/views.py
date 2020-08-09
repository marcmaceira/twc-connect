from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

event_r = requests.get("https://www.eventbrite.com/d/dc--washington/free--food-and-drink--events--this-week/happy-hour/?page=1")
event_soup = BeautifulSoup(event_r.content, 'html.parser')

# Create list for events
eventbrite = []

# Find all events
events = event_soup.find_all('div', {'class':'search-event-card-wrapper'})

for event in events:
    event_title = event.find("div", {"class":"eds-is-hidden-accessible"})
    event_time = event.find("div", {"class":"eds-text-color--primary-brand eds-l-pad-bot-1 eds-text-weight--heavy eds-text-bs"})
    event_location = event.find("div", {"class":"card-text--truncated__one"})
    event_image = event.find("img", {"class": "eds-event-card-content__image"})
    event_url = event.find("a", {"class": "eds-event-card-content__action-link"})
    event_details = {}
    event_details['event_title'] = event_title.text
    event_details['event_time'] = event_time.text
    event_details['event_location'] = event_location.text
    event_details['event_image'] = event_image.get('data-src')
    event_details['event_url'] = event_url.get('href')
    # Append event details dictionary to eventbrite list of events
    eventbrite.append(event_details)

def index(req):
    return render(req, 'events/index.html', {'events':eventbrite})