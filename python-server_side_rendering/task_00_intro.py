#!bin/bash/python3
"""Word replacement function"""
import os
import logging

attendees = [
    {"name": "Alice", "event_title": "Python Conference",
     "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop",
     "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit",
     "event_date": None, "event_location": "Boston"}
]


def generate_invitations(template, attendees):
    if not isinstance(template, str):
        logging.error('Template is invalid string input,'
                      'no output files generated.')
        return
    if (
        not isinstance(attendees, list)
        or not all(isinstance(item, dict) for item in attendees)
    ):
        logging.error('Attendees is invalid list, no output files generated.')
        return

    if not template.strip():
        logging.error('Template is empty, no output files generated.')
        return
    if not attendees:
        logging.error('No data provided, no output files generated.')
        return

    for index, attendee in enumerate(attendees, start=1):
        # replace missing values with n/a
        name = attendee.get("name", "N/A") or "N/A"
        title = attendee.get("event_title", "N/A") or "N/A"
        date = attendee.get("event_date", "N/A") or "N/A"
        location = attendee.get("event_location", "N/A") or "N/A"

        filled_template = (
            template
            .replace("{name}", name)
            .replace("{event_title}", title)
            .replace("{event_date}", date)
            .replace("{event_location}", location)
        )
        # output to file
        output_path = f"output_{index}.txt"
        with open(output_path, "w") as f:
            f.write(filled_template)
