import requests

url = "https://liquipedia.net/valorant/api.php?"
payload = {"parse":"query", "prop":"text"}

r = requests.get(url, params=payload)
print(r.text)