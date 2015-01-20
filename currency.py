rates = [('USD,', 'EUR', 0.86),
         ('EUR', 'USD', 1.15),
         ('USD', 'JPY', 118.68),
         ('GBP', 'USD', 1.51),
         ('USD', 'CHF', 0.87),
         ('USD', 'CAD', 1.21),
         ('EUR', 'JPY', 137.08),
         ('AUD', 'USD', 0.82)]


def convert(rates, value, start, to):
    """Takes a rate from a list of exchange rates and applies it to a value by
    by converting from the "start" variable to the "to" variable by the
    corresponding rate."""
    if start == to:
        return value
