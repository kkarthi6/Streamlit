import yfinance as yf
import streamlit as st

st.sidebar.write("App developed by Kavin Karthikeyan")

st.sidebar.write("Code available on [Github](https://github.com/kkarthi6)")

st.sidebar.write("Connect with me on:")

st.sidebar.write("[Linkedin](https://www.linkedin.com/in/kavin-karthikeyan/)")

st.sidebar.write("[Github](https://github.com/kkarthi6)")

st.sidebar.write("[Twitter](https://twitter.com/kkarthi96)")

st.title("Stock Analyzer")

st.header("Receive detailed report on a stock in seconds")

st.subheader("Enter the stock ticker symbol and the data range for which the price is needed")

t = st.text_input("Please enter the stock ticker symbol(i.e. AAPL):")
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = t
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
sd = st.date_input("Please enter the start date for stock price:")
ed = st.date_input("Please enter the end date for stock price:")
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start = sd, end= ed)
# Open	High	Low	Close	Volume	Dividends	Stock Splits


# show stock prices for the selected date range
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

# get stock info
st.write("Sector:")
tickerData.info["sector"]

# get historical market data
hist = tickerData.history(period="max")

# show actions (dividends, splits)
tickerData.actions

# show dividends
#tickerData.dividends

# show splits
#tickerData.splits

# show financials
tickerData.financials
tickerData.quarterly_financials

# show major holders
tickerData.major_holders

# show institutional holders
tickerData.institutional_holders

# show balance sheet
tickerData.balance_sheet
tickerData.quarterly_balance_sheet

# show cashflow
tickerData.cashflow
tickerData.quarterly_cashflow

# show earnings
tickerData.earnings
tickerData.quarterly_earnings

# show sustainability
tickerData.sustainability

# show analysts recommendations
tickerData.recommendations

# show next event (earnings, etc)
tickerData.calendar
