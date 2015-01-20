rates = [('USD', 'EUR', 0.86),
         ('USD', 'JPY', 118.68),
         ('GBP', 'USD', 1.51),
         ('USD', 'CHF', 0.87),
         ('USD', 'CAD', 1.21),
         ('EUR', 'JPY', 137.08),
         ('AUD', 'USD', 0.82)]


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
    """Takes a value and applies the correct exchange rate and returns the
    result."""
    rate = get_rate(start, to)
    if start == to:
        return value
    else:
        rate = get_rate(start, to)
        return value * rate
