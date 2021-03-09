"""For the 'Holiday' class"""
import configure
import requests
import json
from datetime import datetime

class Holiday():
    """"""

    key = configure.config["key_holiday"]
    now = datetime.now()  # current date and time
    y = int(now.strftime("%Y")) - 1
    m = int(now.strftime("%d"))
    d = int(now.strftime("%d"))

    @staticmethod
    def getHoliday():
        """"""
        url = "https://holidayapi.com/v1/holidays"
        #
        r = requests.get(url,
                         params={"country": "RU",
                                 "key": Holiday.key,
                                 "year": Holiday.y,
                                 "month": Holiday.m,
                                 "day": Holiday.d})
        holiday = json.loads(r.text)

        print(holiday)

Holiday.getHoliday()
