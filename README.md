# Centennial Park Lap Splits (Strava) # 

This Python script retrieves lap split data for the famous Centennial Park Loop in Sydney, Australia, using the Strava API. The script fetches athlete data, calculates lap times, and provides averages and fastest laps for each activity.

## Features

Retrieves and processes lap splits for Centennial Park Loop (Strava Segment ID: 2524690).

Outputs the fastest lap and average lap time for each activity.

Collects data on other athletes for comparison.

Displays detailed lap-by-lap analysis for the current athlete.

## Prerequisites

Python 2.x

The stravalib library for interacting with the Strava API. Install it via pip:

pip install stravalib


A valid Strava access token. You can obtain one by following the steps on the Strava API documentation
.

# How It Works

Authentication: The script uses a Strava access token to authenticate and interact with the Strava API.

Data Fetching: It fetches all lap split data (segment efforts) for the Centennial Park Loop from the Strava API.

Lap Time Calculations:

Each lap is processed to calculate the time in seconds.

The script tracks the fastest lap for each activity and calculates the average lap time.

# Display Output:

The script prints lap-by-lap details, including fastest lap times, average lap times, and the number of laps.

At the end, it provides a summary of the fastest laps and average lap times for all activities.

# Usage

Clone this repository or download the script file.

Ensure you have Python 2.x installed and the required dependencies (stravalib).

Run the script from the command line, passing your Strava access token as the argument:

python centennial_lap_splits.py <YOUR_ACCESS_TOKEN>


Replace <YOUR_ACCESS_TOKEN> with your actual Strava access token.

Example:
python centennial_lap_splits.py abc123xyz456


The script will print detailed information about the Centennial Park Loop laps for the authenticated athlete.

Example Output:

John Doe, 12345
Name: Centennial Park Loop (Segment ID: 2524690)
Other Athletes: Jane Smith, Michael Lee
Laps: 3

    Lap time: 00:04:30
    Lap time: 00:04:20
    Lap time: 00:04:15

Fastest Lap: 00:04:15
Average Lap: 00:04:22
===========================
...
#####################
Average Laps:
00:04:22 Centennial Park Loop 
Fastest Ever Laps:
00:04:15 Centennial Park Loop Jane Smith, Michael Lee

