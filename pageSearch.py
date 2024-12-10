import requests
from reExpression import find_card_in_text

def find_cards_on_webpage(url):
    try:
        if not isinstance(url, str):
            raise TypeError("The URL must be a string.")

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        cards = find_card_in_text(response.text)
        if cards:
            print("Found cards on the page:", cards)
        else:
            print("No cards addresses were found on the page.")

    except requests.Timeout:
        print("Error: The request timed out. Please check your connection or try a different URL.")
    except requests.ConnectionError:
        print("Error: Unable to connect to the server. Please check your internet connection.")
    except requests.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except TypeError as e:
        print(f"Type error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    url = input("Enter the URL of the web page: ")
    find_cards_on_webpage(url)