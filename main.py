"""Just the fitst attempt to get values in CLI"""
import currencies as cr


def Printing(currencies, crypto_currencys):
    print("-"*35, "\n", '{0: ^35}'.format("CURRENCIES"))
    for key, value in currencies.items():
        print("  " + key + "  :", "%.3f" % value)
    bit = crypto_currencys["bit"]
    eth = crypto_currencys["eth"]
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


if __name__ == "__main__":
    currencies = cr.Currencies.getNormalCurrency()
    crypto_currencys = cr.Currencies.getCryptoCurrency()
    Printing(currencies, crypto_currencys)
    input("\nPress enter to exit :3")

