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

#buy sell function 
def buy_sell(data):
    buy_list=[]
    sell_list=[]
    flag_long=False
    flag_short=False
    for i in range(0,len(data)):
        if(data['MIDDLE_SMA'][i]<data['LONG_SMA'][i] and data['SHORT_SMA']<data['MIDDLE_SMA'][i] and flag_long==False and flag_short==False):
            buy_list.append(data['Close'][i])
            sell_list.append(np.nan)
            flag_short=True
        elif flag_short==True and data['SHORT_SMA'][i]>data['MIDDLE_SMA'][i]:
            sell_list.append(data['Close'])
            buy_list.append(np.nan)
            flag_short=False
        elif(data['MIDDLE_SMA'][i]>data['LONG_SMA'][i] and data['SHORT_SMA']>data['MIDDLE_SMA'][i] and flag_long==False and flag_short==False):
            buy_list.append(data['Close'][i])
            sell_list.append(np.nan)
            flag_long=True
        elif flag_long==True and data['SHORT_SMA'][i]<data['MIDDLE_SMA'][i]:
            sell_list.append(data['Close'])
            buy_list.append(np.nan)
            flag_long=False
        else: 
            buy_list.append(np.nan)
            sell_list.append(np.nan)
    return buy_list,sell_list

buy_sell(data)

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
 

