# Weather Microservice

This microservice provides a simple weather data using the free NOAA Weather.gov API.
You can request weather information for a specific **LAT** and **LONG** and optionally request tmrw's forcast

NO API KEY IS NEEDED

# Installation
**After cloning:**
pip install -r requirements.txt 

.\.venv\Scripts\Activate to use on powershell

This will install all the dependecies you need to run it.

**Query Parameters**
Params:
1. lat - required - float
2. lon - required = float
3. tmrw - optional - boolean (default to false)

# Example Request: 
/api/weather?lat=x&lon=7&tmrw=true

tmrw is default to false.

# Response:
```json
    {
        "number": 1,
        "name": "Overnight",
        "startTime": "2025-11-16T00:00:00-08:00",
        "endTime": "2025-11-16T06:00:00-08:00",
        "isDaytime": false,
        "temperature": 56,
        "temperatureUnit": "F",
        "temperatureTrend": "",
        "probabilityOfPrecipitation": {
        "unitCode": "wmoUnit:percent",
            "value": 75
        },
        "windSpeed": "10 mph",
        "windDirection": "SW",
        "icon": "https://api.weather.gov/icons/land/night/rain,80?size=medium",
        "shortForecast": "Rain",
        "detailedForecast": "Rain. Mostly cloudy, with a low around 56. Southwest wind around 10 mph, with gusts as high as 18 mph. Chance of precipitation is 80%. New rainfall amounts between a half and three quarters of an inch possible."
    }
```