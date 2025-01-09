import streamlit as st
import requests


api = "ywrZqqe9l5CShqAmZ6gWD2Z7bVO93jZHn98OFjgI"
url = f"https://api.nasa.gov/planetary/apod?api_key={api}"


response = requests.get(url)
response = response.json()

title = response["title"]
description = response["explanation"]
image = response["url"]

# Download the image
#
# response2 = requests.get(image)
# with open("image.jpg","wb") as file:
#     file.write(response2.content)



st.title(title)
st.image(image)
st.write(description)
