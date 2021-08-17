# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 15:39:36 2021

@author: Harish
"""

import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date
from datetime import timedelta

st.set_page_config(layout="wide")

start = date.today() - timedelta(days = 1)
end = date.today()


st.write("""
         # Stock Price App
         
         Shown are the **Closing Price** and **Volume**
         
         """)

sentence = st.text_input("""Enter the Company Ticker""") 

if sentence:
    tickerSymbol = sentence
else:
    tickerSymbol = 'a'


tickerData = yf.Ticker(tickerSymbol)

name = tickerData.info
st.write(name['longName'])

cp = "Current Price: " + str(name['currentPrice']) + " " + str(name['currency'])
reco = "Recommendation: " + str(name['recommendationKey'])

col1, col2 = st.columns(2)
col1.write(cp)
col2.write(reco)


period = ['1d', '5d', '1m', '6m', 'ytd', '1y', '5y', 'max']
col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
if col1.button('1D'):
    period = 'id'
    start = date.today() - timedelta(days = 1)
    end = date.today()
if col2.button('5D'):
    period = '5d'
    start = date.today() - timedelta(days = 5)
    end = date.today()
if col3.button('1M'):
    period = '1m'
    start = date.today() - timedelta(days = 30)
    end = date.today()
if col4.button('6M'):
    period = '6m'
    start = date.today() - timedelta(days = 180)
    end = date.today()
if col5.button('YTD'):
    period = 'ytd'
    start = date.today() - timedelta(days = 360)
    end = date.today()
if col6.button('1Y'):
    period = '1y'
    start = date.today() - timedelta(days = 360)
    end = date.today()
if col7.button('5Y'):
    period = '5y'
    start = date.today() - timedelta(days = 2000)
    end = date.today()
if col8.button('MAX'):
    period = 'max'
    start = date.today() - timedelta(days = 3600)
    end = date.today()



tickerDf = tickerData.history(period='period', start=start, end=end)

col1, col2 = st.columns(2)

col1.header("Closing Price")
col1.line_chart(tickerDf.Close)

col2.header("Volume")
col2.line_chart(tickerDf.Volume)
