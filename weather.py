"""For the 'Weather' class"""
import configure
import requests
import json

class Weather():
    """Get info about the top news"""

    key = configure.config["key_weather"]

    @staticmethod
    def getWeather():
        """Gets the weather (curent and forecast)"""
        url = "http://api.weatherapi.com/v1/forecast.json"
        # All weather
        r = requests.get(url,
                         params={"q": "Saint-Petersburg",
                                 "key": Weather.key,
                                 "days": "10"})
        weather = json.loads(r.text)
        w_now = weather["current"]
        w_forecast = weather["forecast"]["forecastday"]

        # Current weather
        weather_now = {"temp_c": w_now["temp_c"], "feelslike_c": w_now["feelslike_c"],
                       "text": w_now["condition"]["text"], "icon": w_now["condition"]["icon"],
                       "wind_kph": w_now["wind_kph"], "pressure_mb": w_now["pressure_mb"],
                       "humidity": w_now["humidity"], "cloud": w_now["cloud"]}
        with open(f"pictures/weather.png", "wb") as f:
            try:
                f.write(requests.get(f"http:{weather_now['icon']}").content)
            except:
                pass
        # Forecast weather
        weather_forecast = []
        for w in w_forecast:
            d = {"date": w["date"], "avgtemp_c": w["day"]["avgtemp_c"], "avghumidity": w["day"]["avghumidity"],
                 "daily_chance_of_rain": w["day"]["daily_chance_of_rain"], "sunrise": w["astro"]["sunrise"],
                 "sunset": w["astro"]["sunset"]}
            weather_forecast.append(d)

        return weather_now, weather_forecast

Weather.getWeather()

