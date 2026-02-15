#!/usr/bin/python3
"""Simple Templating Program"""
import os
def generate_invitations(template, attendees):
    """Generates invitation template"""
    #make sure template is string
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return

    #attendees must be list
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list.")
        return

    # check attendees conation dict
    for x, attendee in enumerate(attendees):
        if not isinstance(attendee, dict):
            print("Error: Attendee at index {i} is not a dictionary.".format(x))
            return

    # template shouldnt be empty
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # attendace must be defined
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for x , attendee in enumerate(attendees,1):
        invitation = template
        # variables
        name = attendee.get('name', 'N/A')
        event_title = attendee.get('event_title', 'N/A')
        event_date = attendee.get('event_date', 'N/A')
        event_location = attendee.get('event_location', 'N/A')
        # replace it
        invitation = invitation.replace('{name}', name)
        invitation = invitation.replace('{event_title}', event_title)
        invitation = invitation.replace('{event_date}', event_date)
        invitation = invitation.replace('{event_location}', event_location)
        #create filename
        filename = f"output_{x}.txt"
        try:
            with open(filename, 'w') as file:
                file.write(invitation)
            print(f"Generated invitation file {filename}")
        except Exception as e:
            print(f"Error writing file {filename}:{e}")
