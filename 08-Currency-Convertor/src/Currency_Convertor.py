import requests
from cachetools import cached, TTLCache
import time
from datetime import datetime


# ---------------------------------
# Cache
# ---------------------------------
cache = TTLCache(maxsize=100, ttl=3*60*60)  #* 3 hours that is 60 Minutes and 60 Seconds

# ---------------------------------
# Get Exchange Rate
# ---------------------------------
@cached(cache)
def get_exchange_rate(base_currency, target_currency):
    time.sleep(2)
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    if response.status_code != 200:
        return None, None
    
    update_time = datetime.now()
    return float(response.json()['rates'][target_currency]), update_time


def convert_currency(amount, exchange_rate):
    return float(amount) * float(exchange_rate)


def clear_cache():
    cache.clear()



if __name__ == '__main__':
    base_currency = input("Enter base currency: ").upper()
    target_currency = input("Enter target currency: ").upper()
    amount = float(input("Enter amount: "))
    exchange_rate, update_time = get_exchange_rate(base_currency, target_currency)
    if exchange_rate is not None:
        converted_amount = convert_currency(amount, exchange_rate)
        print(f"{amount} {base_currency}" f"is {converted_amount:.2f}" f"{target_currency}")
        print(f"Last updated: " f"{update_time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("❌ Error fetching exchange rate.")
    
