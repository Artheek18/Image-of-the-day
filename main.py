import streamlit as st
import  requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

api_key = os.getenv("NASA_API_KEY")
date = st.date_input("Select a date", datetime.date.today())
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"

response = requests.get(url)
#print(response.content)
content = response.json()

#print(content['title'])
#print(content['url'])
#print(content['date'])
#print(content['explanation'])


st.title(content['title'])
st.subheader(content['date'])

if content["media_type"] == "image":
    st.image(content["url"])
else:
    st.video(content["url"])

st.write(content['explanation'])

