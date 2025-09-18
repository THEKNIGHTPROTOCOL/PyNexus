import requests 

class CurrencyConverter: 
    """
    A currency converter class that fetches exchange rates from the Fixer.io API.
    """
    def __init__(self, access_key):         
        """
        Initializes the CurrencyConverter with an API access key.

        Args:
            access_key (str): Your access key for the Fixer.io API.
        """
        self.base_url = "http://data.fixer.io/api/latest"
        self.access_key = access_key
        self.rates = self._fetch_rates()

    def _fetch_rates(self):
        """
        Fetches the latest exchange rates from the Fixer.io API.

        Returns:
            dict: A dictionary of exchange rates, or an empty dictionary if fetching fails.
        """
        try:
            params = {'access_key': self.access_key}
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
            data = response.json()

            if data.get("success"):
                return data["rates"]
            else:
                error_info = data.get("error", {})
                print(f"Error fetching rates: {error_info.get('info', 'Unknown error')}")
                return {}
        except requests.exceptions.RequestException as e:
            print(f"Network error or invalid URL: {e}")
            return {}
        except ValueError as e:
            print(f"Error parsing JSON response: {e}")
            return {}

    def convert(self, from_currency, to_currency, amount):
        """
        Converts an amount from one currency to another.

        Args:
            from_currency (str): The currency to convert from (e.g., 'USD', 'EUR').
            to_currency (str): The currency to convert to (e.g., 'INR', 'JPY').
            amount (float or int): The amount to convert.

        Returns:
            float: The converted amount, or None if conversion is not possible.
        """
        if not self.rates:
            print("Exchange rates not available. Please check your internet connection or access key.")
            return None

        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        if from_currency not in self.rates:
            print(f"Error: '{from_currency}' is not a valid currency code or not available.")
            return None
        if to_currency not in self.rates:
            print(f"Error: '{to_currency}' is not a valid currency code or not available.")
            return None

        try:
            # Fixer.io's free plan uses EUR as the base currency.
            # Convert from_currency to EUR, then from EUR to to_currency.
            amount_in_eur = amount / self.rates[from_currency]
            converted_amount = round(amount_in_eur * self.rates[to_currency], 2)
            print(f'{amount} {from_currency} = {converted_amount} {to_currency}')
            return converted_amount
        except KeyError as e:
            print(f"Error: Missing rate for currency {e}. This should ideally not happen if checks pass.")
            return None
        except TypeError:
            print("Error: Amount must be a number.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred during conversion: {e}")
            return None

if __name__ == "__main__":
    YOUR_ACCESS_KEY = "YOUR_ACCESS_KEY"  # Replace with your actual Fixer.io access key

    if YOUR_ACCESS_KEY == "YOUR_ACCESS_KEY":
        print("WARNING: Please replace 'YOUR_ACCESS_KEY' with your actual Fixer.io access key.")
        print("You can get one from: https://fixer.io/signup/free")
        exit()

    converter = CurrencyConverter(YOUR_ACCESS_KEY)

    # Example Usage:
    while True:
        try:
            amount_input = input("Enter amount to convert (or 'q' to quit): ")
            if amount_input.lower() == 'q':
                break
            amount = float(amount_input)
            if amount <= 0:
                print("Please enter a positive amount.")
                continue

            from_country = input("From Currency (e.g., USD, EUR, INR): ").strip().upper()
            to_country = input("To Currency (e.g., JPY, AUD, GBP): ").strip().upper()

            converter.convert(from_country, to_country, amount)
            print("-" * 30)

        except ValueError:
            print("Invalid amount. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
