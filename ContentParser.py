from bs4 import BeautifulSoup

class ContentParser:
    def __init__(self, html_content):
        self.html_content = html_content

    def parse_prices(self):
        soup = BeautifulSoup(self.html_content, "html.parser")
        price_elements = soup.find_all("strong")  # Adjust the selector as needed
        prices = [element.text for element in price_elements]
        return prices if prices else ["Prices not found"]
