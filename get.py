import streamlit as st
import requests

api_key = "KqyujBuf3jXBLbwUTYiADMpLbSJgs6bylOKp95Bf"

url= f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)

content = response.json()
print(content)

title = content["title"]
image = content["url"]
explanation = content["explanation"]

#Download image

image_filepath = "img.png"
image_url = requests.get(image)

with open(image_filepath, "wb") as file:
    file.write(image_url.content)
