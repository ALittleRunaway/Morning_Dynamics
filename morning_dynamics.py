"""Trying to get everything into the UI"""
from PyQt5.QtGui import QPixmap

from datetime import datetime

import configure
import currencies as cr
import news as nw
import weather as wt
import requests
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication


def newsUI():
    news = []
    articles = nw.News.getNews()
    for article in articles:
        news.append(article)
    return news


def UI():
    Form, Window = uic.loadUiType("morning_dynamics.ui")

    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()

    # myLabel->setText("<a href=\"http://example.com/\">Click Here!</a>");
    news = newsUI()
    form.label_news_title_1.setText(news[0]['title'] + " " + f"<a href='{news[0]['url']}'>~</a>")
    form.label_news_1.setText(news[0]["description"])
    form.label_news_title_2.setText(news[1]['title'] + " " + f"<a href='{news[1]['url']}'>~</a>")
    form.label_news_2.setText(news[1]["description"])
    form.label_news_title_3.setText(news[2]['title'] + " " + f"<a href='{news[2]['url']}'>~</a>")
    form.label_news_3.setText(news[2]["description"])
    form.label_news_title_4.setText(news[3]['title'] + " " + f"<a href='{news[3]['url']}'>~</a>")
    form.label_news_4.setText(news[3]["description"])
    form.label_news_title_5.setText(news[4]['title'] + " " + f"<a href='{news[4]['url']}'>~</a>")
    form.label_news_5.setText(news[4]["description"])

    try:
        pixmap = QPixmap("pictures/news_1.jpg")
        form.label_picture_1.setPixmap(pixmap)
    except:
        pass
    try:
        pixmap = QPixmap("pictures/news_2.jpg")
        form.label_picture_2.setPixmap(pixmap)
    except:
        pass
    try:
        pixmap = QPixmap("pictures/news_3.jpg")
        form.label_picture_3.setPixmap(pixmap)
    except:
        pass
    try:
        pixmap = QPixmap("pictures/news_4.jpg")
        form.label_picture_4.setPixmap(pixmap)
    except:
        pass
    try:
        pixmap = QPixmap("pictures/news_5.jpg")
        form.label_picture_5.setPixmap(pixmap)
    except:
        pass

    currencies = cr.Currencies.getNormalCurrency()
    crypto_currencies = cr.Currencies.getCryptoCurrency()

    form.label_usd_rub.setText(str("%.3f" % currencies['USD_RUB']))
    form.label_eur_rub.setText(str("%.3f" % currencies['EUR_RUB']))
    form.label_usd_byn.setText(str("%.3f" % currencies['USD_BYN']))
    form.label_eur_byn.setText(str("%.3f" % currencies['EUR_BYN']))

    form.bit_price.setText(str("%.3f" % crypto_currencies['bit']['price']))
    form.bit_1h.setText(str("%.3f" % crypto_currencies['bit']['percent_change_1h']))
    form.bit_24h.setText(str("%.3f" % crypto_currencies['bit']['percent_change_24h']))
    form.bit_7d.setText(str("%.3f" % crypto_currencies['bit']['percent_change_7d']))
    form.bit_30d.setText(str("%.3f" % crypto_currencies['bit']['percent_change_30d']))

    form.eth_price.setText(str("%.3f" % crypto_currencies['eth']['price']))
    form.eth_1h.setText(str("%.3f" % crypto_currencies['eth']['percent_change_1h']))
    form.eth_24h.setText(str("%.3f" % crypto_currencies['eth']['percent_change_24h']))
    form.eth_7d.setText(str("%.3f" % crypto_currencies['eth']['percent_change_7d']))
    form.eth_30d.setText(str("%.3f" % crypto_currencies['eth']['percent_change_30d']))

    now = datetime.now()  # current date and time
    d = now.strftime("%d %B %Y")
    form.date.setText(d)

    weather_now, weather_forecast = wt.Weather.getWeather()

    try:
        pixmap = QPixmap(f"pictures/weather.png")
        form.label_weather_icon.setPixmap(pixmap)
    except:
        pass

    form.temp.setText(str(weather_now["temp_c"]))
    form.feels_like.setText(str(weather_now["feelslike_c"]))
    form.wind.setText(str(weather_now["wind_kph"]))
    form.humidity.setText(str(weather_now["humidity"]))
    form.ch_of_rain.setText(str(weather_forecast[0]["daily_chance_of_rain"]))
    form.sunrise.setText(weather_forecast[0]["sunrise"])
    form.sunset.setText(weather_forecast[0]["sunset"])
    form.weather_text.setText(weather_now["text"])

    form.tm_temp.setText(str(weather_forecast[1]["avgtemp_c"]))
    form.tm_humidity.setText(str(weather_forecast[1]["avghumidity"]))
    form.tm_ch_of_rain.setText(str(weather_forecast[1]["daily_chance_of_rain"]))

    form.atm_temp.setText(str(weather_forecast[2]["avgtemp_c"]))
    form.atm_humidity.setText(str(weather_forecast[2]["avghumidity"]))
    form.atm_ch_of_rain.setText(str(weather_forecast[2]["daily_chance_of_rain"]))

    app.exec()

if __name__ == "__main__":
    try:
        UI()
        input()
    except (requests.exceptions.ConnectionError):
        print("No network")
        input()
