"""For the 'Currencies' class"""
import configure
import requests
import json

class Currencies():
    """Get the info about the required currencies"""

    key = configure.config["key"]
    key_cryp = configure.config["key_cryp"]

    @staticmethod
    def getNormalCurrency():
        """Get normal currencies"""
        url = "https://free.currconv.com/api/v7/convert"
        # Russian rubble
        r = requests.get(url,
                         params={"q": "USD_RUB,EUR_RUB",
                                 "compact": "ultra",
                                 "apiKey": Currencies.key})
        # print(r.status_code, end=" ")
        cur_rub = json.loads(r.text)
        # Belarussian ruble
        r = requests.get(url,
                         params={"q": "USD_BYN,EUR_BYN",
                                 "compact": "ultra",
                                 "apiKey": Currencies.key})
        # print(r.status_code)
        cur_byn = json.loads(r.text)
        # Unite currencies in one dictionary
        return {**cur_rub, **cur_byn}

    @staticmethod
    def getCryptoCurrency():
        """Get crypto currency"""
        url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
        # Bitcoin
        r = requests.get(url,
                         params={"symbol": "BTC",
                                 "CMC_PRO_API_KEY": Currencies.key_cryp
                                 })
        # print(r.status_code, end=" ")
        bit = json.loads(r.text)
        cur_bit = bit["data"]["BTC"]["quote"]["USD"]
        del cur_bit["market_cap"], cur_bit["last_updated"], cur_bit["volume_24h"]
        # Ethereum
        r = requests.get(url,
                         params={"symbol": "ETH",
                                 "CMC_PRO_API_KEY": Currencies.key_cryp
                                 })
        # print(r.status_code)
        eth = json.loads(r.text)
        cur_eth = eth["data"]["ETH"]["quote"]["USD"]
        del cur_eth["market_cap"], cur_eth["last_updated"], cur_eth["volume_24h"]
        return {"bit": cur_bit, "eth": cur_eth}
