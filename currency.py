rates = [('USD', 'EUR', 0.86)]


def get_rate(start, to):
    """Returns the exchange rate based on the starting currency to the ending
    currency."""
    for tup in rates:
        if start == tup[0] and to == tup[1]:
            rate = tup[2]
            return rate
        elif start == tup[1] and to == tup[0]:
            rate = round(1/tup[2], 2)
            return rate



def convert(rates, value, start, to):
    """Takes a rate from a list of exchange rates and applies it to a value by
    by converting from the "start" variable to the "to" variable by the
    corresponding rate."""
    rate = get_rate(start, to)
    if start == to:
        return value
    else:
        rate = get_rate(start, to)
        return value * rate
