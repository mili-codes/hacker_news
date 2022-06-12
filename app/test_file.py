import json
import requests
from http.client import HTTPSConnection

end_point = "/api/etf"
url = "www.nseindia.com"

payload=''
headers = {
  'authority': 'www.nseindia.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'referer': 'https://www.nseindia.com/market-data/exchange-traded-funds-etf',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin'
}
conn = HTTPSConnection(url)

conn.request("GET",end_point,payload, headers)

# response = requests.request("GET", url1 )
# response = requests.request("GET", url )

res = conn.getresponse()
data = res.read().decode("utf-8")
print((data))
with open("etfs.json", "w") as f:
    json.dump(json.loads(data), f)
