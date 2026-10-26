# Imports
import json
from getpass import getpass
import os
from pathlib import Path
from playwright.sync_api import sync_playwright, Playwright
import time

#PATHS
CREDS = Path("data/credential.json")
COURSES = Path("data/courses.json")
URL = "https://experience.elluciancloud.com/illinois/"


# # Credential Input
# data = {}
# data['user'] = getpass("Username: ")
# data['pass'] = getpass("Password: ")

# CREDS.parent.mkdir(parents=True, exist_ok=True)
# CREDS.touch(exist_ok=True)

# with open(CREDS, "w") as json_file:
#     json.dump(data, json_file, indent=4)

# del data
# # Courses to check
# courses = []

# while True:
#     course = input("Course: ")

#     if course == "":
#         break

#     courses.append({
#         "course": course
#     })

# COURSES.parent.mkdir(parents=True, exist_ok=True)

# with open(COURSES, "w") as json_file:
#     json.dump(courses, json_file, indent=4)

# del courses

#Navigating to Page
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(URL)

    while True:

        time.sleep(1)

        try:
            with open("data/credential.json", "r") as json_file:
                page.locator('input[name="upn"]').fill(f"{data['user']}@illinois.edu")
                page.get_by_label("Remember my choice").check()

        except KeyboardInterrupt:
            break

        except Exception as e:
            print("Error:", e)
