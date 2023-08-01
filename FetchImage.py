import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

page = 20

def save_image(url, filename):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.thumbnail((100, 100))
    img.save(filename)

def fetch_google_images(query, start):
    url = f"https://www.google.com/search?q={query}&tbm=isch&start=" + str(start)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    image_elements = soup.find_all("img", class_="yWs4tf")
    for i, image_element in enumerate(image_elements):
        image_url = image_element.get("src")
        if image_url:
            save_image(image_url, f"headimg/head_img_index{start+i}.png")

query = "头像"
for i in range(5):
    fetch_google_images(query, i*page)

