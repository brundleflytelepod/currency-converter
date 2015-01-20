from currency import *

rates = [('USD', 'EUR', 0.86),
         ('USD', 'JPY', 118.68),
         ('GBP', 'USD', 1.51),
         ('USD', 'CHF', 0.87),
         ('USD', 'CAD', 1.21),
         ('EUR', 'JPY', 137.08),
         ('AUD', 'USD', 0.82)]


def test_convert_same():
    assert convert(rates[0][2], 1, 'USD', 'USD') == 1


def test_convert_USDtoEUR():
    assert convert(rates[0][2], 1, 'USD', 'EUR') == 0.86


def test_value_other_than_1():
    assert convert(rates[0][2], 2, 'USD', 'EUR') == 1.72


def test_convert_EURtoUSD():
    assert convert(rates[1][2], 1, 'EUR', 'USD') == 1.16


def test_get_rate_normal():
    assert get_rate('USD', 'EUR') == 0.86


def test_get_rate_inverse():
    assert get_rate('EUR', 'USD') == 1.16


def test_convert_GBPtoUSD():
    assert convert(rates, 2, 'GBP', 'USD') == 3.02


def test_convert_USDtoGBP():
    assert convert(rates, 2, 'USD', 'GBP') == 1.32


def test_convert_EURtoJPY():
    assert convert(rates, 3, 'EUR', 'JPY') == 411.24
