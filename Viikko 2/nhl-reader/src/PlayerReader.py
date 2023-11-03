import requests

class PlayerReader:
    def __init__(self, url):
        self.url=url
        self.response=requests.get(url).json()
    