import requests
import streamlit as st

# Prepare the API key and URL for the Astronomy Picture of the Day (APOD)
API_KEY = 'API_KEY'  # Replace with your actual API key
url = (f'https://api.nasa.gov/planetary/apod?'
       f'api_key={API_KEY}')
# Make request
request = requests.get(url)
# Get a dict with data
content = request.json()
# Extract data
title = content['title']
image_url = content['hdurl']
explanation = content['explanation']
# Download the image
request = requests.get(image_url)
image_content = request.content
with open('image.jpg','wb') as file:
       file.write(image_content)
# Display the image and title in Streamlit
st.set_page_config(page_title='Astronomy Image of the Day')
st.title(title)
st.image('image.jpg')
st.write(explanation)