## Introduction

Flight delay analysis plays a crucial role in aviation operations. 
This project demonstrates an end-to-end real-time flight delay analysis system using the OpenSky Network API, Python, MySQL, and Power BI.

## Problem Statement

Most flight delay analysis systems rely on historical data and fail to reflect current air traffic conditions. 
This project addresses the need for a system that collects, stores, and analyzes live flight data in real time.

## Objectives
Collect real-time flight data using OpenSky API
Store live data in a MySQL database
Analyze flight movement and status (on-ground vs airborne)
Identify country-wise air traffic density
Visualize insights using Power BI dashboards

## Data Source
API: https://opensky-network.org/api/states/all
Format: JSON
Type: Real-time flight state data
Frequency: Every 60 seconds

## Tools & Technologies
Python (Data Extraction & Processing)
Requests (API communication)
Pandas (Data manipulation)
MySQL (Database storage)
Jupyter Notebook (Development)
Power BI (Visualization)


## System Architecture
OpenSky API → Python → Data Cleaning → MySQL → Power BI Dashboard



## Database Design
Table: flight_data
Column Name	     DataType	            Description
id	             INT (PK)	             Auto increment
icao24	         VARCHAR(10)	         Aircraft ID
callsign	       VARCHAR(10)           Flight number
origin_country	 VARCHAR(50)           Country of origin
latitude	       FLOAT	               Latitude
longitude	       FLOAT              	 Longitude
baro_altitude	   FLOAT	               Altitude
velocity	       FLOAT	               Speed
on_ground	       BOOLEAN	             Ground status
true_track	     FLOAT	               Direction
vertical_rate	   FLOAT	               Climb/Descent
collected_time	 DATETIME	             Data capture time

## Data Collection (Python)
url = "https://opensky-network.org/api/states/all"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data["states"])

## Data Cleaning
Handle missing values (fillna())
Remove irrelevant columns
Convert data types
Standardize timestamps


## Key Analysis & Insights
Flight Status
Majority flights are airborne
Smaller portion on-ground

## Top Countries by Flight Count
United States
United Kingdom
Ireland

## Delay Insights
~3.3% flights are delayed
Maximum delay ≈ 125 minutes
Delay mostly from specific regions

## Correlation
Velocity vs Delay → ~0.02
Very weak relationship

## Outliers
Extreme delays identified using IQR
Helps detect unusual flight behavior

## MySQL Integration
df.to_sql(
    name='flight_data',
    con=engine,
    if_exists='append',
    index=False

## Power BI Dashboard Features
KPI Cards (Total Flights, Avg Delay)
Country-wise analysis
Map visualization (air traffic)
Filters (Country, Delay, Status)
Time-based trends


## Key Results
High traffic from US & Europe
On-ground flights show near-zero velocity
Clear peak traffic times
Efficient large-scale data handling using MySQL

## Limitations
API request limits
No direct delay data
No weather/airport integration

## Future Enhancements
Weather data integration
Machine learning delay prediction
Real-time alerts (SQL triggers)
Cloud deployment
)



## Real-Time-Flight-Delay-Analysis-System/
│
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 .gitignore
│
├── data/
│   ├── live_flight_data.csv
│   ├── cleaned_flight_data.csv
│
├── notebooks/
│   ├── liveflight_data_analysis.ipynb
│
├── scripts/
│   ├── fetch_data.py
│   ├── clean_data.py
│   ├── analysis.py
│   ├── db_upload.py
│
├── sql/
│   ├── queries.sql
│
├── dashboard/
│   ├── flight_data_powerbi_dashboard.pbix
│
└── images/
    ├── dashboard1.png
  
