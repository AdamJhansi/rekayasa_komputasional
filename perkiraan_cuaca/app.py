from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#OpenWeatherMap API
def get_weather(city):
    api_key = "fa224e7e72e703e20692e9f04779e929" 
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        weather_data = get_weather(city)
        if weather_data["cod"] == 200:
            weather = {
                "city": weather_data["name"],
                "temperature": weather_data["main"]["temp"],
                "description": weather_data["weather"][0]["description"],
                "icon": weather_data["weather"][0]["icon"],
                "wind": (weather_data["wind"]["speed"])*3.6 
            }
            print(weather)
            return render_template("index.html", weather=weather)
        else:
            return render_template("index.html", error="Kota tidak ditemukan.")
    else:
        return render_template("index.html")
    
if __name__ == "__main__":
    app.run(debug=True)
