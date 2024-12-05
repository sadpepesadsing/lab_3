import re

pattern = r'\b\d{4}\s\d{4}\s\d{4}\s\d{4}\b'

def is_valid_card(card: str):
    try:
        if not isinstance(card, str):
            raise TypeError("card must be str!")
        return re.match(pattern, card) is not None
    except TypeError as e:
        print(f"Error: {e}")
        return False

def find_card_in_text(text: str):
    try:
        if not isinstance(text, str):
            raise TypeError("The provided text must be a string.")
        return re.findall(pattern, text)
    except TypeError as e:
        print(f"Error: {e}")
        return []