import requests
import selectorlib
import time
import pandas as pd
import streamlit as st
import plotly.express as px

URL = "http://programmer100.pythonanywhere.com/"
def scrape(url):
    response = requests.get(url)
    return response.text

def extract(html):
    extractor = selectorlib.Extractor.from_yaml_file(r"F:\App\Practise\Scrape_Temperature_Data\extract.yaml")
    data = extractor.extract(html)
    return data['temperature']

def write(file, data):
    time.currnet_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(file, 'a') as f:
        f.write(f"{time.currnet_time}, {data}\n")

def read(file):
    df = pd.read_csv(file, names=['Time', 'Temperature'])
    return df

if __name__ == "__main__":
    while True:
        html = scrape(URL)
        temperature = extract(html)
        write(r"F:\App\Practise\Scrape_Temperature_Data\data.txt", temperature)
        df = read(r"F:\App\Practise\Scrape_Temperature_Data\data.txt")
        fig = px.line(df, x='Time', y='Temperature(C)', title='Temperature Over Time')
        st.plotly_chart(fig)
        time.sleep(5)