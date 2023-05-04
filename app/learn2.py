# def learn(n):
#     try:
#         x= 458741/n
#     except Exception as e:
#         return e
#     else:
#         print(f"not sure how it works {x}")
#     return x


# print(learn(1))

# z = {
#       "symbol": "LICNETFGSC",
#       "assets": "GSEC10 NSE Index",
#       "open": "22",
#       "high": "23.3",
#       "low": "21.74",
#       "ltP": "22.65",
#       "chn": "0.84",
#       "per": "3.85",
#       "qty": "103368",
#       "trdVal": "2326813.68",
#       "nav": "21.7591",
#       "wkhi": "26.94",
#       "wklo": "19",
#       "yPC": 2.8610354223433196,
#       "mPC": 4.09007352941175,
#       "prevClose": "21.81",
#       "nearWKH": 15.924276169265044,
#       "nearWKL": -19.21052631578947,
#       "date30dAgo": "02-Jun-2022",
#       "perChange30d": 2.98,
#       "meta": None
# }

# b ={
#         "symbol": "LICNETFGSC",
#         "companyName": "LIC MF - LIC MF G-sec LT ETF - GO",
#         "activeSeries": [
#           "EQ"
#         ],
#         "debtSeries": [],
#         "tempSuspendedSeries": [],
#         "isin": "INF767K01MV5"
#       }

# s = z.keys()

# # print(s)

# l = ['symbol', 'assets', 'open', 'high', 'low', 'ltP', 'chn', 'per', 'qty', 'trdVal', 'nav', 'wkhi', 'wklo', 'yPC', 'mPC', 'prevClose', 'nearWKH', 'nearWKL', 'date30dAgo', 'perChange30d', 'meta.companyName', 'meta.isin']

# l = [1,2,3,4,5]

# g = ",".join(map(str,l))

# print(g)

file_path = 'input.txt'

with open(file_path, 'r') as f:
    data = f.readlines()

for i in data:
    print(i)