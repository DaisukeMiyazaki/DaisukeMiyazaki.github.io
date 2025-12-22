---
layout: post
title: "Calendar Auto Route Calculator: Automatically Add Travel Time to Google Calendar"
date: 2025-12-22
lang: en
genre: practical
excerpt: 'I created a Google Apps Script (GAS) tool that automatically calculates the route (train/walk) to your scheduled events and adds "Travel to..." blocks to your Google Calendar.'
---

https://gist.github.com/DaisukeMiyazaki/4293e05627ecae17b23dd8b234a29a12

This is a Google Apps Script (GAS) tool that automatically calculates the travel route (train/walk) to an event when you add it to Google Calendar, and adds a **"Travel to..."** event to your calendar.

## Features

1.  **Automatic Route Calculation**
    - Reads the "Location" of the event and searches for a route using the Google Maps API.
    - Automatically determines the starting point from "Home (default)" or "Location of the previous event (if events are back-to-back)".
2.  **Arrive 15 Minutes Early**
    - Schedules travel time so that you arrive at the destination **15 minutes before** the event starts.
3.  **Detailed Route Guidance**
    - Automatically adds the train time, line name, transfer station, and fare (if available) to the Description field of the calendar event.
4.  **Automatic Return Route**
    - Automatically creates a travel plan (Travel to Home) to return home after the last event of the day ends.
5.  **Duplicate Prevention**
    - Does not double-register if a travel plan has already been created.

## Setup Instructions

This tool requires no server and runs on Google Apps Script.

### 1. Create a Project

1.  Access [Google Apps Script (script.google.com)](https://script.google.com/) in your browser.
2.  Create a "New Project".

### 2. Install the Code

1.  Copy the contents of `calendar_auto_route.js` from this repository.
2.  Paste everything into `Code.gs` in the GAS editor.

### 3. Change Settings

Rewrite the constants at the beginning of the code to match your environment.

```javascript
const CALENDAR_ID = "primary"; // Leave as is if using your own calendar
const HOME_LOCATION = "Ofuna Station, Kamakura"; // Address of your home or nearest station
```

### 4. Enable Service

To use Google Maps functions, the following steps may be required (currently, the standard `Maps` class is often used, so additional settings are often unnecessary, but just in case).

- Click the "+" button in "Services" on the left menu -> Add "Google Maps Service" if available (usually not required).

### 5. Trigger Settings (Automation)

1.  Click the clock icon (Trigger) on the left menu.
2.  Click the "Add Trigger" button.
3.  Set as follows and save:
    - Function to run: `onCalendarChange`
    - Event source: `From calendar`
    - Event type: `Event updated`
4.  You will be asked for permission to access your Google account when saving, so "Allow" it.
    - _If "This app is not verified by Google" appears, click "Advanced" -> "Go to (Project Name)" and allow it._

## Usage

1.  Add an event to Google Calendar. Be sure to fill in the **"Location"** field.
2.  After a few seconds to tens of seconds, a new event called "Travel to [Event Name]" will be automatically added immediately before that event.
3.  Click on the added event to check "what time to catch the train" in the details field.

## Notes

- When the trigger fires, scan events from today to 14 days later.
- Find events that have a "Location" and do not have "Travel to" immediately before them, and process them.
- Route search uses `Maps.newDirectionFinder()` (Transit Mode).
- Outbound search uses `.setArrive(start - 15min)`, return uses `.setDepart(end)`.
