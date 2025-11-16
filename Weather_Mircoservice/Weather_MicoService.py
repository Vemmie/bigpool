from flask import Flask, request, jsonify
import requests

# on the terminal type: curl http://127.0.0.1:5002/
app = Flask(__name__)

# gets a current weather and condition of a given location long / lat
@app.route('/api/weather', methods = ['GET'])
def getWeather():
    # example: /api/weather?lat=x&lon=7&tmrw=true
    # Get lat and long from query params
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    # default will be false
    tmrw = request.args.get('tmrw', 'false').lower() == 'true'

    if not lat or not lon:
        return jsonify({"Error" : "Please provide lat and lon params"}), 400

    # checking for correct typees for lat and lon
    try:
        # Convert to float
        lat = float(lat)
        lon = float(lon)
    except ValueError:
        return jsonify({"Error" : "Invalid lat or lon values"}), 400

    # Call the weather API
    url = f"https://api.weather.gov/points/{lat},{lon}"
    weatherResponse = requests.get(url)
    if weatherResponse.status_code != 200:
        return jsonify({"Error" : "Failed to retrieve weather data"}), 500
    
    # get the forcast URL from the weather response
    forecastUrl = weatherResponse.json()['properties']['forecast']
    forecastReponse = requests.get(forecastUrl)
    if forecastReponse.status_code != 200:
        return jsonify({"Error" : "Failed to retrieve weather data"}), 500
    
    period = forecastReponse.json()['properties']['periods'], 200

    if not tmrw:
        return jsonify(period[0])
    else:
        return jsonify(period[1])

'''
example json of forcast to use
"periods": [
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
    ]
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) # Change 5004 to your desired port number