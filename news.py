"""For the 'News' class"""
import configure
import requests
import json

class News():
    """Get info about the top news"""

    key = configure.config["key_news"]

    @staticmethod
    def getNews():
        """Get top 5 news in technology"""
        url = "https://newsapi.org/v2/top-headlines"
        # Technology news
        r = requests.get(url,
                         params={"sortBy": "popularity",
                                 "pageSize": 5,
                                 "apiKey": News.key,
                                 "category": "technology",
                                 # "sourses": "bbc-news",
                                 # "domains": "bbc.com",
                                 "language": "en"})
        news = json.loads(r.text)
        articles_buff = news["articles"]
        articles = []
        # Unite news in one list
        i = 0
        for article in articles_buff:
            articles.append({"title": article["title"], "description": article["description"], "url": article["url"],
                             "urlToImage": article["urlToImage"], "publishedAt": article["publishedAt"]})
            i += 1
            # with open(f"pictures/{''.join(article['title'][:10].split())}.jpg", "wb") as f:
            with open(f"pictures/news_{i}.jpg", "wb") as f:
                try:
                    f.write(requests.get(article["urlToImage"]).content)
                except:
                    pass
        return articles

News.getNews()