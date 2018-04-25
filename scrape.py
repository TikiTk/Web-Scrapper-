payload = {"email": "##number##", "password": "##number##"}

import requests
from lxml import html
from bs4 import beautifulsoup4

session_requests = requests.session()

login_url = "https://badoo.com/signin/"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)

result = session_requests.post(login_url, payload, headers=dict(refer=login_url))

print(result)

pages = requests.get("https://badoo.com/encounters", params=dict(query="web scraping",page=2))


