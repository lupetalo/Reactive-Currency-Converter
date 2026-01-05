import requests
import json
import re
import os

# URL of the NBS Middle Rate page
URL = "https://webappcenter.nbs.rs/ExchangeRateWebApp/ExchangeRate/CurrentMiddleRate"
JSON_PATH = "rates.json"

def get_existing_currencies():
    if not os.path.exists(JSON_PATH):
        print(f"{JSON_PATH} not found.")
        return []
    
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)
    
    # Return keys from the rates object
    return list(data.get("rates", {}).keys())

def fetch_and_update():
    currencies_to_update = get_existing_currencies()
    if not currencies_to_update:
        print("No currencies found to update.")
        return

    print(f"Fetching rates from {URL}...")
    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        html = response.text
    except Exception as e:
        print(f"Error fetching data: {e}")
        return

    # Store fetched RSD values here
    rsd_rates = {}

    # We always need EUR to calculate the base. If it's not in the JSON, we must fetch it anyway.
    if "EUR" not in currencies_to_update:
        currencies_to_update.append("EUR")

    print(f"Updating rates for: {', '.join(currencies_to_update)}")

    for currency in currencies_to_update:
        if currency == "RSD":
            # RSD is the quote currency of the NBS list (1 unit = 1 RSD? No, NBS list gives value of X units in RSD)
            # Actually, NBS gives "Middle Exchange Rate" which is "How many RSD for 1 Unit of Foreign Currency"
            # So for RSD itself, the rate is 1. We don't fetch it.
            rsd_rates["RSD"] = 1.0
            continue
            
        # Regex to find rate. 
        # Pattern looks for the currency code in a cell, then eventually the rate.
        # <td>CURRENCY</td> ... <td>rate</td>
        pattern = r"<td>" + re.escape(currency) + r"</td>\s*<td>\d+</td>\s*<td>.*?</td>\s*<td>\d+</td>\s*<td>([0-9,]+)</td>"
        
        match = re.search(pattern, html, re.DOTALL)
        if match:
            rate_str = match.group(1).replace(',', '.')
            rsd_rates[currency] = float(rate_str)
            # print(f"Found {currency}: {rsd_rates[currency]} RSD")
        else:
            if currency != "EUR": # Don't spam if we can't find obscure ones, but warn for EUR
                print(f"Warning: Could not find rate for {currency} on NBS page.")
    
    if "EUR" not in rsd_rates:
        print("Critical Error: Could not find EUR rate. Cannot calculate base rates.")
        return

    # Base is EUR.
    # rsd_rates["EUR"] = 117.3 (meaning 1 EUR = 117.3 RSD)
    # rsd_rates["USD"] = 100.3 (meaning 1 USD = 100.3 RSD)
    
    # We want rates relative to EUR (where EUR = 1).
    # If 1 EUR = 117.3 RSD
    # Then 1 RSD = 1/117.3 EUR
    # Value of USD in EUR?
    # 1 USD = 100.3 RSD = 100.3 * (1/117.3 EUR) = 0.85 EUR?
    # WAIT. rates.json uses the convention: "How much of Quote Currency (USD) for 1 Base Currency (EUR)?"
    # If EUR is base (1), and USD is 1.16, it means 1 EUR = 1.16 USD.
    
    # Let's re-verify.
    # 1 EUR = 117.3 RSD
    # 1 USD = 100.3 RSD
    # 1 EUR = (117.3 / 100.3) USD = 1.168 USD.
    # Formula: Rate_in_JSON = (EUR_in_RSD) / (Currency_in_RSD)

    eur_in_rsd = rsd_rates["EUR"]
    
    # Reload data to preserve structure
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)
    
    updated_rates = data.get("rates", {})
    
    # Update RSD explicitly first
    # 1 EUR = 117.3 RSD
    updated_rates["RSD"] = round(eur_in_rsd, 4)
    updated_rates["EUR"] = 1

    for currency, rsd_val in rsd_rates.items():
        if currency == "EUR" or currency == "RSD":
            continue
        
        # Calculate cross rate
        new_rate = eur_in_rsd / rsd_val
        updated_rates[currency] = round(new_rate, 4)
        print(f"Updated {currency}: {updated_rates[currency]}")

    data["rates"] = updated_rates
    
    with open(JSON_PATH, 'w') as f:
        json.dump(data, f, indent=4)
        
    print("\nSUCCESS: rates.json updated.")

if __name__ == "__main__":
    fetch_and_update()
