import unittest
from src.converter import supported_currencies, get_rate, convert, convert_to_many


class TestRates(unittest.TestCase):
    def test_supported_currencies(self):
        self.assertIn("INR", supported_currencies())
        self.assertEqual(len(supported_currencies()), 5)

    def test_get_rate(self):
        self.assertEqual(get_rate("USD", "JPY"), 150.0)
        self.assertEqual(get_rate("EUR", "GBP"), 0.8889)


class TestConvert(unittest.TestCase):
    def test_usd_to_eur(self):
        self.assertEqual(convert(100, "USD", "EUR"), 90.0)

    def test_eur_to_usd(self):
        self.assertEqual(convert(90, "EUR", "USD"), 100.0)

    def test_same_currency(self):
        self.assertEqual(convert(50, "USD", "USD"), 50.0)

    def test_lowercase_codes(self):
        self.assertEqual(convert(100, "usd", "eur"), 90.0)

    def test_convert_to_many(self):
        self.assertEqual(
            convert_to_many(100, "USD", ["EUR", "INR"]),
            {"EUR": 90.0, "INR": 8500.0},
        )


class TestErrorHandling(unittest.TestCase):
    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            convert(-10, "USD", "EUR")

    def test_unsupported_currency(self):
        with self.assertRaises(ValueError):
            convert(100, "USD", "XYZ")

    def test_non_numeric_amount(self):
        with self.assertRaises(ValueError):
            convert("100", "USD", "EUR")


if __name__ == "__main__":
    unittest.main()
