import pandas as pd
import numpy as np
from matplotlib import pyplot as pp
from DateTime import DateTime
pp.style.use('fivethirtyeight')

apple=pd.read_csv('AAPL.csv')
print(apple)

#Simple moving average for 30 days
SMA30=pd.DataFrame()
SMA30['Adj Close']=apple['Adj Close'].rolling(window=30).mean()

#Simple moving average for 100days
SMA100=pd.DataFrame()
SMA100['Adj Close']=apple['Adj Close'].rolling(window=100).mean()

#Visualization
pp.figure(figsize=(12.5,4.5))
pp.plot(apple['Adj Close'],label='Apple')
pp.plot(SMA30['Adj Close'],label='SMA30')
pp.plot(SMA100['Adj Close'],label='SMA100')
pp.title('Adj Close Price Visualization')
pp.xlabel('From Sep,1984 To 29th Mar,2008')
pp.ylabel('Adj Close Price in USD $')
pp.legend(loc='upper left')
print(pp.show())

#Storing Data in one frame
data=pd.DataFrame()
data['apple']=apple['Adj Close']
data['SMA30']=SMA30['Adj Close']
data['SMA100']=SMA100['Adj Close']

#Signal to Buy or Sell Share
def buy_sell(data):
    signalToBuy=[]
    signalToSell=[]
    flag=-1
    for i in range(len(data)):
        if data['SMA30'][i]>data['SMA100'][i]:
            if flag !=1:
                signalToBuy.append(data['apple'][i])
                signalToSell.append(np.nan)
                flag=1
            else:
                signalToBuy.append(np.nan)
                signalToSell.append(np.nan)
        elif data['SMA30'][i]<data['SMA100'][i]:
            if flag !=0:
                signalToSell.append(data['apple'][i])
                signalToBuy.append(np.nan)
                flag=0
            else:
                signalToBuy.append(np.nan)
                signalToSell.append(np.nan)
        else:
            signalToBuy.append(np.nan)
            signalToSell.append(np.nan)
    return (signalToBuy,signalToSell)

#Storing Data in new DataSet
buy_sell=buy_sell(data)
data['Buy_Signal_Price']=buy_sell[0]
data['Sell_Signal_Price']=buy_sell[1]

#Visualaization of Data to Sell or Buy
pp.figure(figsize=(14.5,4.6))
pp.plot(data['apple'],label='Apple',alpha=0.35)
pp.plot(data['SMA30'],label='SMA30',alpha=0.35)
pp.plot(data['SMA100'],label='SMA100',alpha=0.35)
pp.scatter(data.index,data['Buy_Signal_Price'],label='Buy',marker='^',color='green')
pp.scatter(data.index,data['Sell_Signal_Price'],label='Sell',marker='v',color='red')
pp.title('According To Adjust Price When to Buy & Sell')
pp.xlabel('From Sep,1984 To 29th Mar,2008')
pp.ylabel('Stock price in US Dollar $')
pp.legend(loc='upper left')
print(pp.show())