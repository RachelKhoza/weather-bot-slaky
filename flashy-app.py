import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# OpenWeather API key export your key with env variable
API_KEY = os.getenv("API_KEY_WEATHER")

@app.route("/weather", methods=["POST"])
def weather():
    city = request.form.get("text")
    if not city:
        return jsonify({"text": "Please provide a city name."})

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        return jsonify({"text": f"Error: {data['message']}"})

    temperature = data["main"]["temp"]
    return jsonify({"text": f"The temp in {city} is {temperature}°C."})

if __name__ == "__main__":
    app.run(debug=True)
