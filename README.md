# 🏃 Centennial Park Lap Splits (Strava)

A Python script that analyzes lap split data for the iconic **Centennial Park Loop** in Sydney, Australia using the Strava API. It fetches athlete activity data, calculates lap times, and highlights performance insights like fastest laps and averages.

---

## 🚀 Features

- Retrieves lap splits for **Centennial Park Loop**  
  *(Strava Segment ID: `2524690`)*
- Calculates:
  - Fastest lap per activity
  - Average lap time
- Compares performance with other athletes
- Displays detailed lap-by-lap breakdown for the authenticated athlete

---

## 🧰 Prerequisites

- **Python 3.x**
- **stravalib** library  
  Install via pip:
  ```bash
  pip install stravalib
  ```
- **Strava Access Token**  
  Obtain one by following the [Strava API documentation](https://developers.strava.com/docs/)

---

## ⚙️ How It Works

1. **Authentication**  
   Uses your Strava access token to authenticate with the API.

2. **Data Fetching**  
   Retrieves all segment efforts for the Centennial Park Loop.

3. **Lap Time Calculations**  
   - Converts lap durations to seconds  
   - Tracks fastest lap per activity  
   - Computes average lap time

---

## 📊 Output

The script prints:

- Lap-by-lap details
- Fastest and average lap times
- Number of laps per activity
- Summary across all activities

**Example Output:**
```
John Doe, 12345
Name: Centennial Park Loop (Segment ID: 2524690)
Other Athletes: Jane Smith, Michael Lee
Laps: 3

    Lap time: 00:04:30
    Lap time: 00:04:20
    Lap time: 00:04:15

Fastest Lap: 00:04:15
Average Lap: 00:04:22

...

Average Laps:
00:04:22 Centennial Park Loop 

Fastest Ever Laps:
00:04:15 Centennial Park Loop — Jane Smith, Michael Lee
```

---

## 🧪 Usage

1. Clone this repository or download the script.
2. Ensure Python 3.x and `stravalib` are installed.
3. Run the script with your Strava access token:
   ```bash
   python centennial_lap_splits.py <YOUR_ACCESS_TOKEN>
   ```
   Replace `<YOUR_ACCESS_TOKEN>` with your actual token.

**Example:**
```bash
python centennial_lap_splits.py abc123xyz456
```
