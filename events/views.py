from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

event_r = requests.get("https://www.eventbrite.com/d/dc--washington/free--food-and-drink--events--this-week/happy-hour/?page=1")
event_soup = BeautifulSoup(event_r.content, 'html.parser')

event_title_div = event_soup.find_all("div", {"class":"eds-is-hidden-accessible"})
event_time_div = event_soup.find_all("div", {"class":"eds-text-color--primary-brand eds-l-pad-bot-1 eds-text-weight--heavy eds-text-bs"})
event_location_div = event_soup.find_all("div", {"class":"card-text--truncated__one"})
event_image_div = event_soup.find_all("img", {"class": "eds-event-card-content__image"})
event_url_div = event_soup.find_all("a", {"class": "eds-event-card-content__action-link"})
event_name = []
event_time = []
event_location = []
event_image = []
event_url = []

for th in event_title_div:
    event_name.append(th.text)

del event_name[::2]

for e_time in event_time_div:
    event_time.append(e_time.text)

del event_time[::2]

for e_location in event_location_div:
    event_location.append(e_location.text)

del event_location[::2]

for img in event_image_div:
    event_image.append(img.get('data-src'))

del event_image[::2]

for a in event_url_div:
    event_url.append(a.get('href'))

del event_url[::2]
del event_url[::2]

x = list(zip(event_name, event_time, event_location, event_image, event_url))

def index(req):
    return render(req, 'events/index.html', {'event':x})