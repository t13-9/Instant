import streamlit as st
import yfinance as yf
import pandas as pd

st.title("lil finance dashboard")
st.title('_This_ is :blue[cool] :sunglasses:')

dropDown = ("TSLA", "AAPLE", "MSFT", "BTC-USD","ETH-USD")
dropDownMenu = st.multiselect("Pick your assets", dropDown)

start = st.date_input("Start", value = pd.to_datetime('2021-01-01'))
end = st.date_input("End", value = pd.to_datetime('today'))

def relativert(df):
    rel = df.pct_change(fill_method ='ffill')
    cumret = (1+rel).cumprod() -1
    cumret = cumret.fillna(0)
    return cumret

if len(dropDownMenu) > 0:
    df = relativert(yf.download(dropDown, start, end)['Adj Close'])
    st.header('Returns of {}'.format(dropDownMenu))
    st.line_chart(df)