"""Just the fitst attempt to get values in CLI"""
import currencies as cr
import news as nw
import requests


class Printing():
    """Prints the main information"""

    currencies = cr.Currencies.getNormalCurrency()
    crypto_currencys = cr.Currencies.getCryptoCurrency()
    articles = nw.News.getNews()

    @staticmethod
    def printingCurrencies():
        """prints currencies"""
        print("#"*35, "\n", '{0: ^35}'.format("CURRENCIES"))
        for key, value in Printing.currencies.items():
            print("  " + key + "  :", "%.3f" % value)
        bit = Printing.crypto_currencys["bit"]
        eth = Printing.crypto_currencys["eth"]
        print("-"*35, "\n", '{0: ^35}'.format("BITCOIN"))
        for key, value in bit.items():
            if "price" in key:
                sign = "$"
            else:
                sign = "%"
            print(" ", '{0: <19}'.format(key), ":", "%.3f" % (value), sign)
        print("-"*35, "\n", '{0: ^35}'.format("ETHERIUM"))
        for key, value in eth.items():
            if "price" in key:
                sign = "$"
            else:
                sign = "%"
            print(" ", '{0: <19}'.format(key), ":", "%.3f" % (value), sign)

    @staticmethod
    def printingNews():
        """prints News"""
        print("\n", "#"*35, "\n", '{0: ^35}'.format("NEWS"))
        for article in Printing.articles:
            print("    ", article["title"], "\n", article["description"], "\n",
                  article["url"], "\n", article["publishedAt"], "\n")

    @staticmethod
    def printingAll():
        """prints everything"""
        Printing.printingCurrencies()
        Printing.printingNews()


if __name__ == "__main__":
    try:
        Printing.printingAll()
        input()
    except (requests.exceptions.ConnectionError):
        print("No network")
        input()

