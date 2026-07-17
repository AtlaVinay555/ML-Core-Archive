import matplotlib.pyplot as plt
import requests
import pandas as pd
from datetime import date
 
def convert(x):
    try:
        return float(x)
    except:
        return x
        
def ch(x):
    #19-Sep-16
    m = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,\
    'Oct':10,'Nov':11,'Dec':12}
    y = x.split('-')
    return(date(int('20'+y[2]), m[y[1]], int(y[0])))
 
def graph_date(stock):
    url = 'https://www.google.com/finance/historical?output=csv&q='+stock
    resp = requests.get(url)
    data = resp.text.split('\n')    
    fields = data[0].split(',')
    df_data = df_list = []
    
    for each in data[1:]:
        df_data = [convert(x) for x in each.split(',')]
        if len(df_data)==6:
            df_list.append(df_data)
            
    df_stocks = pd.DataFrame(df_list, columns=fields, index=range(1,len(df_list)+1))
    print df_stocks['Date']
    df_stocks['Date'] = map(ch, df_stocks['Date'])
    print df_stocks['Date']
       
    plt.plot_date(df_stocks['Date'],df_stocks['Open'],'-')
    plt.xlabel('date')
    plt.ylabel('price')
    plt.show()
    
graph_date('TSLA')



'''

import matplotlib.pyplot as plt

from io import StringIO

import numpy as np

import urllib

import urllib.request

import matplotlib.dates as mdates

from datetime import datetime

def bytespdate2num(fmt,encoding='utf-8'):
  def bytesconverter(b):
    s = b.decode(encoding)
    return mdates.date2num(datetime.strptime(s, fmt))
  return bytesconverter

def graph_data(stock):

  stock_price = 'https://pythonprogramming.net/yahoo_finance_replacement'

  source_code = urllib.request.urlopen(stock_price).read().decode()

  stock_data = []
  split_source = source_code.split('\n')

  for line in split_source:
    split_line = line.split(',')
    if(len(split_line)) == 6:
      if 'values' not in line and 'labels' not in line:
        stock_data.append(line)

  date , closep, highp, lowp, openp, volume = np.loadtxt(
    StringIO('\n'.join(stock_data)),
    delimiter=',',
    unpack=True,
    converters={0:bytespdate2num('%Y%m%d')}
  )

  plt.plot_date(date,closep,'-',label='Price')

  plt.xlabel('Date')

  plt.ylabel('Price')

  plt.title('Graph\nSub-Title')

  plt.legend()

  plt.show()

graph_data('TSLA')

'''