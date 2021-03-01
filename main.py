"""Trying to get everything into the UI"""
from PyQt5.QtGui import QPixmap

from datetime import datetime


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
    form.label_news_title_1.setText(f"<a href='{news[0]['url']}', color='black'>{news[0]['title']}</a>")
    form.label_news_1.setText(news[0]["description"])
    form.label_news_title_2.setText(f"<a href='{news[1]['url']}'>{news[1]['title']}</a>")
    form.label_news_2.setText(news[1]["description"])
    form.label_news_title_3.setText(f"<a href='{news[2]['url']}'>{news[2]['title']}</a>")
    form.label_news_3.setText(news[2]["description"])
    form.label_news_title_4.setText(f"<a href='{news[3]['url']}'>{news[3]['title']}</a>")
    form.label_news_4.setText(news[3]["description"])
    form.label_news_title_5.setText(f"<a href='{news[4]['url']}'>{news[4]['title']}</a>")
    form.label_news_5.setText(news[4]["description"])

    try:
        pixmap = QPixmap(f"pictures/{''.join(news[0]['title'][:10].split())}.jpg")
        form.label_picture_1.setPixmap(pixmap)
    except:
        pass
    try:
        pixmap = QPixmap(f"pictures/{''.join(news[1]['title'][:10].split())}.jpg")
        form.label_picture_2.setPixmap(pixmap)
    except:
        pass
    try:
        pixmap = QPixmap(f"pictures/{''.join(news[2]['title'][:10].split())}.jpg")
        form.label_picture_3.setPixmap(pixmap)
    except:
        pass
    try:
        pixmap = QPixmap(f"pictures/{''.join(news[3]['title'][:10].split())}.jpg")
        form.label_picture_4.setPixmap(pixmap)
    except:
        pass
    try:
        pixmap = QPixmap(f"pictures/{''.join(news[4]['title'][:10].split())}.jpg")
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

    app.exec()

if __name__ == "__main__":
    try:
        UI()
        input()
    except (requests.exceptions.ConnectionError):
        print("No network")
        input()
