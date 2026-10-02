RATES = {
    "USD": 1.0,
    "EUR": 0.9,
    "GBP": 0.8,
    "INR": 85.0,
    "JPY": 150.0,
}


def _validate(amount, *currencies):
    """Check that the amount is a valid number and the currencies are supported."""
    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a number")
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    for code in currencies:
        if code.upper() not in RATES:
            raise ValueError(f"Unsupported currency: {code}")


def supported_currencies():
    """Return the list of supported currency codes."""
    return sorted(RATES.keys())


def get_rate(from_currency, to_currency):
    """Return the exchange rate from one currency to another."""
    _validate(1, from_currency, to_currency)
    rate = RATES[to_currency.upper()] / RATES[from_currency.upper()]
    return round(rate, 4)


def convert(amount, from_currency, to_currency):
    """Convert an amount from one currency to another, rounded to 2 decimals."""
    _validate(amount, from_currency, to_currency)
    rate = RATES[to_currency.upper()] / RATES[from_currency.upper()]
    return round(amount * rate, 2)


def convert_to_many(amount, from_currency, to_currencies):
    """Convert one amount into several currencies at once."""
    return {code.upper(): convert(amount, from_currency, code) for code in to_currencies}
