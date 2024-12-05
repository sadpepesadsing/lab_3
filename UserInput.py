from reExpression import is_valid_card

def check_user_input():
    card = input("Enter your card: ")

    if not isinstance(card, str):
        raise TypeError("The entered value must be a string.")
    if is_valid_card(card):
        print("The card is correct!")
    else:
        print("Incorrect card.")


if __name__ == "__main__":
    check_user_input()