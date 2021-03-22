sudo apt-get install python3-bs4

# Importing streamlit 
import streamlit as st
import streamlit.components as stc

# Importing beautifulsoup 
from bs4 import BeautifulSoup

# Importing other necessary dependencies
import numpy as np
import pandas as pd
import base64
import time
from time import sleep
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

# Imporitng and setting up Selenium
import selenium
from selenium import webdriver 
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)

#Function to download the file as csv
def csv_downloader(data,name):
    csvfile = data.to_csv()
    b64 = base64.b64encode(csvfile.encode()).decode()
    timestr = time.strftime("%Y%m%d-%H%M%S")
    timestr = name+timestr
    new_filename = "AutoScraper_{}_.csv".format(timestr)
    st.markdown("#### Download as CSV ####")
    href = f'<a href = "data:file/csv;base64,{b64}" download = "{new_filename}">Click to download CSV</a>'
    st.markdown(href,unsafe_allow_html=True)

# Streamlit app
def main():
    
    st.sidebar.write("App developed by Kavin Karthikeyan")    
    menu = ["Home","S&P 500","Dow 30","NASDAQ 100","Crypto","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "Home":
        st.subheader("Home")
        st.write("Welcome to Stockbot")
        
    elif choice == "S&P 500":
        st.subheader("S&P 500")
        driver.get("https://www.slickcharts.com/sp500")
        
        df = pd.read_html(driver.page_source)[0]
        df = df.head(500)
        st.dataframe(df)
        csv_downloader(df,"S&P 500")
        driver.quit()

    elif choice == "Dow 30":
        st.subheader("Dow 30")
        driver.get("https://www.cnbc.com/dow-30/")
        
        df = pd.read_html(driver.page_source)[0]
        df = df.head(30)
        st.dataframe(df)
        csv_downloader(df,"Dow 30")
        driver.quit()

    elif choice == "NASDAQ 100":
        st.subheader("NASDAQ 100")
        driver.get("https://www.slickcharts.com/nasdaq100")
        
        df = pd.read_html(driver.page_source)[0]
        df = df.head(100)
        st.dataframe(df)
        csv_downloader(df,"NASDAQ 100")
        driver.quit()

    elif choice == "Crypto":
        st.subheader("Cryptocurrenices")
        driver.get("https://www.slickcharts.com/currency")
    
        df = pd.read_html(driver.page_source)[0]
        df = df.head(100)
        st.dataframe(df)
        csv_downloader(df,"Crypto")
        driver.quit()

    else:
        st.write("About")
        st.write("THANKS FOR VISITING STOCK-BOT")
        st.write("Code available on [Github](https://github.com/kkarthi6/Streamlit/blob/51e014589d2f0b95ee8c4de94209dfd53d38b2a0/Streamlit_stock_app.py)")
        st.write("Connect on")
        st.write("[Linkedin](https://www.linkedin.com/in/kavin-karthikeyan/)")
        st.write("[Github](https://github.com/kkarthi6)")
        st.write("[Twitter](https://twitter.com/kkarthi96)")
    

if __name__ == '__main__':
    main()

