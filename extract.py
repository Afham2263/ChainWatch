import requests

def extract_coin_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": "false"
         
     }
     
    response = requests.get(url,params = params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

if __name__ == "__main__":
    coin_data = extract_coin_data()
    for coin in coin_data:
        print(coin["name"], "-", coin["current_price"])