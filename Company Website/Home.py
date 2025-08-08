import streamlit as st
import pandas as pd
st.set_page_config(layout='wide')
title = "The Best Company"
content = "Nothing"
st.title(title)
st.write(content)
st.header('Our Team')
data = pd.read_csv('data.csv',sep=',')
for index in range(0,12,3):
    left, mid, right = st.columns(3)
    with left:
        name = data['first name'][index].strip() + " " + data['last name'][index].strip()
        st.subheader(name.title())
        st.write(data['role'][index])
        st.image(f"images/{data['image'][index]}")
    with mid:
        name = data['first name'][index+1] + data['last name'][index+1]
        st.subheader(name.title())
        st.write(data['role'][index+1])
        st.image(f"images/{data['image'][index+1]}")
    with right:
        name = data['first name'][index+2] + data['last name'][index+2]
        st.subheader(name.title())
        st.write(data['role'][index+2])
        st.image(f"images/{data['image'][index+2]}")