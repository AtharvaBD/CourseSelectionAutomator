# Imports
import json
from getpass import getpass
import os
from pathlib import Path

#PATHS
CREDS = Path("data/credential.json")
COURSES = Path("data/courses.json")

# Credential Input
data = {}
data['user'] = getpass("Username: ")
data['pass'] = getpass("Password: ")

CREDS.parent.mkdir(parents=True, exist_ok=True)
CREDS.touch(exist_ok=True)

with open(CREDS, "w") as json_file:
    json.dump(data, json_file, indent=4)

del data
# Courses to check
courses = []

while True:
    course = input("Course: ")

    if course == "":
        break

    courses.append({
        "course": course
    })

COURSES.parent.mkdir(parents=True, exist_ok=True)

with open(COURSES, "w") as json_file:
    json.dump(courses, json_file, indent=4)

del courses