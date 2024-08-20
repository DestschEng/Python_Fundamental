import requests

url = "http://127.0.0.1:8000/webhook/stock-alert"
data = {
    "symbol": "AAPL",
    "price": 150.5,
    "threshold": 150.0
}

response = requests.post(url, json=data)
print(response.json())
