import re

pattern = r'\b\d{4}\s\d{4}\s\d{4}\s\d{4}\b'
def is_luhn_valid(card_number_string):
    digits = list(map(int, card_number_string.replace(" ", "")))

    sum_of_digits = 0

    for i in range(len(digits)):
        if i % 2 == 0:
            digit = digits[i] * 2
            if digit > 9:
                digit -= 9
            sum_of_digits += digit
        else:
            sum_of_digits += digits[i]
    return sum_of_digits % 10 == 0

def is_valid_card(card: str):
    if not isinstance(card, str):
        raise TypeError("card must be str!")
    return re.match(pattern, card) is not None and is_luhn_valid(card)

def find_card_in_text(text: str):
    if not isinstance(text, str):
        raise TypeError("The provided text must be a string.")
    cards = re.findall(pattern, text)
    for card in cards:
        if not is_luhn_valid(card):
            cards.remove(card)
    return f"Cards: {cards}"