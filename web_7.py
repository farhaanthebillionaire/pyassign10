import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        self.user_agent = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.4324.150 Safari/537.36"
}
        self.response = requests.get(self.url, headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response, "lxml")

    def product_title(self):
        title = self.soup.find("span", {"id": "productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Title Not Found"

    def product_price(self):
        price = self.soup.find("span", {"id": "priceblock_ourprice"})
        if price is None:  # Sometimes Amazon uses a different ID
            price = self.soup.find("span", {"id": "priceblock_dealprice"})
        if price is not None:
            return price.text.strip()
        else:
            return "Price Not Found"


# Example usage
samsung = PriceTracer(
    url="https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B07KK3FCRS/ref=sr_1_1?dchild=1&keywords=samsung+s10e&qid=1613308105&sr=8-4"
)

print("Product Title:", samsung.product_title())
print("Product Price:", samsung.product_price())
