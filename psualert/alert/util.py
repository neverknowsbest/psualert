import feedparser
import datetime

from alert.constants import PSU_TIMELY_FEED_URL
from alert.models import TimelyWarning, Location, WarningType

def parse_full_feed():
    feed = feedparser.parse(PSU_TIMELY_FEED_URL)

    for entry in feed.entries:
        parse_new_entry(entry)
        
def parse_new_entry(entry):
    tw = TimelyWarning()
    tw.date = datetime.strptime(entry.published, "%a, %d %b %Y %I:%M %z")
    tw.permanent_url = entry.link
    tw.title = entry.title
    tw.description = entry.summary
    
    locations, warnings = parse_description(entry.summary)
    tw.location = locations
    tw.warning_type = warnings
    
def parse_description(description):
    pass