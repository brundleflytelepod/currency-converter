rates = [('USD', 'EUR', 0.86),
         ('EUR', 'USD', 1.15)]


def convert(rate, value, start, to):
    """Takes a rate from a list of exchange rates and applies it to a value by
    by converting from the "start" variable to the "to" variable by the
    corresponding rate."""
    rate = [tuples[2]
             for tuples in rates
             if start == tuples[0] and to == tuples[1]]
    if start == to:
        return value
    else:
        return value * rate[0]
