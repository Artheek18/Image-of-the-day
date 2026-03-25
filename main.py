import streamlit as st
import  requests
import os
from dotenv import load_dotenv
import datetime


st.set_page_config(page_title="NASA APOD", page_icon="🌌")
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

# 🔥 Cache function
@st.cache_data
def get_apod(url):
    return requests.get(url, timeout=5).json()
content = get_apod(url)


st.title("NASA Astronomy Picture of the Day")
st.write("Explore NASA's Astronomy Picture of the Day.")
st.subheader(content['date'])
st.header(content['title'])

if content["media_type"] == "image":
    st.image(content["url"], width='stretch')
    if content.get("hdurl"):
        st.link_button("Open HD Image", content["hdurl"])

else:
    st.video(content["url"])

if content.get("copyright"):
    st.caption(f"© {content['copyright']}")

st.write(content['explanation'])

