import requests

class WebFetcher:
    def __init__(self, url):
        self.url = url
        self.html_content = ""

    def fetch_content(self):
        response = requests.get(self.url)
        self.html_content = response.text
        return self.html_content
