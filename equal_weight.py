import numpy as np  
import pandas as pd  
import requests 
import xlsxwriter 
import math
import os 
from dotenv import load_dotenv
load_dotenv()
stocks = pd.read_csv('sp_500_stocks.csv')

symbol='AAPL'
IEX_CLOUD_API_TOKEN=os.getenv('IEX_CLOUD_API_TOKEN')

api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()

my_columns = ['Ticker', 'Price','Market Capitalization', 'Number Of Shares to Buy']

final_dataframe = pd.DataFrame(columns = my_columns)
for symbol in stocks['Ticker'][:5]:
    api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(api_url).json()
    final_dataframe = final_dataframe.append(
                                        pd.Series([symbol, 
                                                   data['latestPrice'], 
                                                   data['marketCap'], 
                                                   'N/A'], 
                                                  index = my_columns), 
                                        ignore_index = True)


print(final_dataframe)