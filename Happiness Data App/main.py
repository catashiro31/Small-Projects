import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('happy.csv', sep=',')

st.title('In Search for Happiness')
country = st.selectbox(label='Country',
                       options=df['country'].sort_values().values)
x_axis = st.selectbox(label='Select the data for the X-axis',
                      options=['GDP','Happiness','Generosity'])
y_axis = st.selectbox(label='Select the data for the Y-axis',
                      options=['GDP','Happiness','Generosity'])
st.subheader(f'{x_axis} and {y_axis}')

figure = px.scatter(x=df[x_axis.lower()], y=df[y_axis.lower()], labels={'x' : x_axis, 'y' : y_axis})
st.plotly_chart(figure)