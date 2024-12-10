import unittest
from unittest.mock import patch, mock_open
import requests
from reExpression import is_valid_card, find_card_in_text
from pageSearch import find_cards_on_webpage
from fileSearch import find_cards_in_file

class TestReCard(unittest.TestCase):
    def test_is_valid_card(self):
        self.assertTrue(is_valid_card("2282 2812 2822 8228"))
        self.assertTrue(is_valid_card("1111 1111 1111 1141"))
        self.assertFalse(is_valid_card("1111 1111 1111 1111"))
        self.assertFalse(is_valid_card("1414 1414 1414 1414"))
        self.assertFalse(is_valid_card("2282 2822 8228 2282"))

    def test_find_cards_in_text(self):
        text = "kasdjfhlkasdfhaklsdh 2282 2812 2822 8228 23847623847623487634823764 1111 1111 1111 1111"
        result = find_card_in_text(text)
        self.assertEqual(result, ["2282 2812 2822 8228"])


class TestFileCardSearch(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="Card: 2282 2812 2822 8228\n1111 1111 1111 1111")
    def test_find_cards_in_file(self, mock_file):
        result = find_cards_in_file('cards.txt')
        self.assertEqual(result, ["2282 2812 2822 8228"])

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_find_cards_in_file_not_found(self, mock_file):
        with patch("builtins.print") as mock_print:
            find_cards_in_file("card.txt")
            mock_print.assert_called_with(
                "Error: The file was not found. Make sure that the path is specified correctly.")

class TestPageCardSearch(unittest.TestCase):
    @patch("requests.get")
    def test_find_cards_on_webpage(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "2202 2055 7215 4331"

        with patch("builtins.print") as mock_print:
            find_cards_on_webpage("https://github.com/sadpepesadsing/lab_3/tree/master")
            mock_print.assert_called_with("Found cards on the page:", ["2202 2055 7215 4331"])

    @patch("requests.get")
    def test_find_cards_on_webpage_error(self, mock_get):
        mock_get.side_effect = requests.RequestException("Network error")

        with patch("builtins.print") as mock_print:
            find_cards_on_webpage("https://github.com/sadpepesadsing")
            mock_print.assert_called_with("An unexpected error occurred: Network error")


if __name__ == "__main__":
    unittest.main()