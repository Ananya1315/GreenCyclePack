import requests

data = {
    "length": 18,
    "width": 10,
    "height": 6
}

response = requests.post("http://127.0.0.1:5000/suggest_box", json=data)
print("Response:", response.json())
