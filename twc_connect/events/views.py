from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

event_r = requests.get("https://www.eventbrite.com/d/dc--washington/events--this-week/happy-hour/?page=1")
event_soup = BeautifulSoup(event_r.content, 'html.parser')

event_title_div = event_soup.find_all("div", {"class":"eds-is-hidden-accessible"})
event_time_div = event_soup.find_all("div", {"class":"eds-text-color--primary-brand eds-l-pad-bot-1 eds-text-weight--heavy eds-text-bs"})
event_location_div = event_soup.find_all("div", {"class":"card-text--truncated__one"})

event_name = []
event_time = []
event_location = []

for th in event_title_div:
    event_name.append(th.text)

del event_name[::2]

for e_time in event_time_div:
    event_time.append(e_time.text)

del event_time[::2]

for e_location in event_location_div:
    event_location.append(e_location.text)

del event_location[::2]

test = [[event_name], [event_time], [event_location]]

x = list(zip(event_name, event_time, event_location))

def index(req):
    return render(req, 'events/index.html', {'event':x})