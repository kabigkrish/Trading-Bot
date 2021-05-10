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
token=os.getenv('IEX_CLOUD_API_TOKEN')
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/quote?token={token}'
data = requests.get(api_url).json()
print(data)  
my_columns = ['Ticker', 'Price','Market Capitalization', 'Number Of Shares to Buy']
final_dataframe = pd.DataFrame(columns = my_columns)
final_dataframe = final_dataframe.append(
                                        pd.Series(['AAPL', 
                                                   data['latestPrice'], 
                                                   data['marketCap'], 
                                                   'N/A'], 
                                                  index = my_columns), 
                                        ignore_index = True)

print(final_dataframe)