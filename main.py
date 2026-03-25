import streamlit as st
import  requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

api_key = os.getenv("NASA_API_KEY")
min_date = datetime.date(1995, 6, 16)

date = st.date_input(
    "Select a date",
    datetime.date.today(),
    min_value=min_date,
    max_value=datetime.date.today()
)

url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={date}"

response = requests.get(url)
content = response.json()


st.title(content['title'])
st.subheader(content['date'])

if content["media_type"] == "image":
    st.image(content["url"])
else:
    st.video(content["url"])

st.write(content['explanation'])

