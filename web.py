import requests

url = "http://127.0.0.1:8000/picture/images/nature-images.jpg"

user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"
}

response = requests.get(url=url, headers=user)
pic = response.content

with open("nature-images.jpg", "wb") as f:
    f.write(pic)

print("Image downloaded successfully as nature-images.jpg")
