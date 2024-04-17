import requests
import json

url = "http://127.0.0.1:5172/exchange/get_exchanges/"

payload = json.dumps({
    "day": 7,
    # "rarity": "common",
    "type": "gloves",
    # "level": 0,
    # "durability": 1,
    # "exchange_left": 3,
    # "order_by": "price"
})
headers = {
    'X-API-KEY': 'cb3e3f68-03e9-4a88-bfae-3dd7ad093f12',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.json())
