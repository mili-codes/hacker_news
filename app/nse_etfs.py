# from nsetools import *
# from nsetools.utils import byte_adaptor
import json
from http.client import HTTPSConnection
import pandas as pd
# from pprint import pprint

class ETF():
    def __init__(self):
        # super().__init__()
        self.nse_url = "www.nseindia.com"
        self.etf_endpoint = "/api/etf"
        self.etf_headers = self._nse_headers()
        self.conn = self._connection()
        self.payload = ''

    def _connection(self):
        conn = HTTPSConnection(self.nse_url)
        conn.request("GET",self.etf_endpoint,headers=self.etf_headers)
        return conn.getresponse()
    
    def _nse_headers(self):
        """
        Builds right set of headers for requesting https://www.nseindia.com/api/etf
        :return: a dict with http headers
        """
        return {
                    'authority': 'www.nseindia.com',
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'referer': 'https://www.nseindia.com/market-data/exchange-traded-funds-etf',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin'
                }

    def get_etf_list(self,as_json=False):
        """
        :return: a list of dictionaries containing ets and their details
        """
        c = 0
        while self.conn.getcode() != 200:
            self.conn = self._connection()
            if c%10 ==0:
                print("please wait connecting", '.'*(c//10), sep="", end="")
            c +=1

        print("Connection successful with code ",self.conn.getcode())
        data = self.conn.read().decode('utf-8')

        return json.loads(data) if as_json else data

        # clean the output and make appropriate type conversions
        # resp_list = [self.clean_server_response(item) for item in res_dict['data']]
        # return data self.render_response(resp_list, as_json)
       

    def get_etf_details(self, symbol):
        """
        :return: details of a etf
        """
        resp_list = self.get_etf_list(as_json=True)
        search_flag = False
        for item in resp_list["data"]:
            if item['symbol'] == symbol.upper():
                search_flag = True
                break
        return item if search_flag else None

    
    def buy_sell(self, symbol):
        if symbol == '': return "enter valid symbol"
        det = self.get_etf_details(symbol)
        # min_ohl_ltp = list(map(float,[det['open'],det['high'],det['low'],det['ltp']]))
        nav, ltp = det['nav'], det['ltP']
        if float(nav) >= float(ltp):
            print(f"buy nav is {nav} and ltp is {ltp}")
        else:
            print(f"sell nav is {nav} and ltp is {ltp}")
    
    def get_etf_json_file(self):
        with open("etf_data_json.json", mode="w") as f:
            json.dump(self.get_etf_list(), f,indent=4)
    
    def get_etf_csv_file(self):
        data = self.get_etf_list(as_json=True)["data"]
        df = pd.json_normalize(data)
        df.to_csv("etf_data_csv.csv")
        


etf = ETF()

sym = etf.buy_sell("mafang")
# etf.get_etf_csv_file()




# import json
# from http.client import HTTPSConnection
# import pandas as pd

# class ETF:
#     def __init__(self):
#         self.nse_url = "www.nseindia.com"
#         self.etf_endpoint = "/api/etf"
#         self.etf_headers = {
#                     'authority': 'www.nseindia.com',
#                     'accept': '*/*',
#                     'accept-language': 'en-US,en;q=0.9',
#                     'referer': 'https://www.nseindia.com/market-data/exchange-traded-funds-etf',
#                     'sec-fetch-mode': 'cors',
#                     'sec-fetch-site': 'same-origin'
#                 }
#         self.conn = self._get_response()
#         self.payload = ''

#     def _get_response(self):
#         conn = HTTPSConnection(self.nse_url)
#         conn.request("GET", self.etf_endpoint, headers=self.etf_headers)
#         return conn.getresponse()

#     def get_etf_list(self, as_json=False):
#         response = self._get_response()
#         data = response.read().decode('utf-8')
#         return json.loads(data) if as_json else data

#     def get_etf_details(self, symbol):
#         resp_list = self.get_etf_list(as_json=True)
#         for item in resp_list["data"]:
#             if item['symbol'] == symbol.upper():
#                 return item
#         return None

#     def buy_sell(self, symbol):
#         if symbol == '': return "Enter valid symbol"
#         det = self.get_etf_details(symbol)
#         if det:
#             nav, ltp = det['nav'], det['ltP']
#             if float(nav) >= float(ltp):
#                 print(f"buy nav is {nav} and ltp is {ltp}")
#             else:
#                 print(f"sell nav is {nav} and ltp is {ltp}")
#         else:
#             print(f"No details found for symbol {symbol}")

#     def get_etf_json_file(self):
#         with open("etf_data_json.json", mode="w") as f:
#             json.dump(self.get_etf_list(), f,indent=4)

#     def get_etf_csv_file(self):
#         data = self.get_etf_list(as_json=True)["data"]
#         df = pd.json_normalize(data)
#         df.to_csv("etf_data_csv.csv")
