import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

ticker = "RBLBANK.NS"
yfObj = yf.Ticker(ticker)
data = yfObj.history(start="2000-01-01", end="2020-12-31")
name = yfObj.info['shortName']


def three_moving_avg(ticker, short_term_sma , mid_term_sma, long_term_sma, start_date='2000-01-01', end_date='2020-12-31'):
    yfObj = yf.Ticker(ticker)
    data = yfObj.history(start=start_date, end=end_date)
    data['SHORT_SMA'] = data['Close'].rolling(short_term_sma).mean()
    data['MIDDLE_SMA'] = data['Close'].rolling(mid_term_sma).mean()
    data['LONG_SMA'] = data['Close'].rolling(long_term_sma).mean()

    return data
short_term_sma =9 
mid_term_sma=21
long_term_sma = 50
data = three_moving_avg(ticker, short_term_sma,mid_term_sma, long_term_sma) 

#export to excel 
#data.to_excel("output.xlsx")  

#visualizing 
plt.figure(figsize=(10, 5))
plt.title('close Price',fontsize=18)
plt.plot(data['Close'],label='close price',color='blue')
plt.plot(data['SHORT_SMA'],label='short_term_sma',color='red')
plt.plot(data['MIDDLE_SMA'],label='mid_term_sma',color='orange')
plt.plot(data['LONG_SMA'],label='long_term_sma',color='green')

plt.title(f'Price Chart for {name}')
plt.xlabel('data',fontsize=18)
plt.ylabel('close price',fontsize=18)
plt.show()



