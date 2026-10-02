import pytest
from src.converter import supported_currencies, get_rate, convert, convert_to_many


def test_supported_currencies():
    assert supported_currencies() == ["EUR", "GBP", "INR", "JPY", "USD"]


def test_get_rate_usd_to_jpy():
    assert get_rate("USD", "JPY") == 150.0


def test_get_rate_eur_to_gbp():
    assert get_rate("EUR", "GBP") == 0.8889


def test_convert_usd_to_eur():
    assert convert(100, "USD", "EUR") == 90.0


def test_convert_usd_to_inr():
    assert convert(100, "USD", "INR") == 8500.0


def test_convert_eur_to_usd():
    assert convert(90, "EUR", "USD") == 100.0


def test_convert_gbp_to_inr():
    assert convert(10, "GBP", "INR") == 1062.5


def test_convert_same_currency():
    assert convert(50, "USD", "USD") == 50.0


def test_convert_zero_amount():
    assert convert(0, "USD", "JPY") == 0.0


def test_convert_lowercase_codes():
    assert convert(100, "usd", "eur") == 90.0


def test_convert_to_many():
    assert convert_to_many(100, "USD", ["EUR", "INR"]) == {"EUR": 90.0, "INR": 8500.0}


def test_negative_amount():
    with pytest.raises(ValueError):
        convert(-10, "USD", "EUR")


def test_unsupported_currency():
    with pytest.raises(ValueError):
        convert(100, "USD", "XYZ")


def test_non_numeric_amount():
    with pytest.raises(ValueError):
        convert("100", "USD", "EUR")
