payload = {"email": "+++++", "password": "+++++"}

import requests
from lxml import html
from bs4 import BeautifulSoup

session_requests = requests.session()

login_url = "https://badoo.com/signin/"
result = session_requests.get(login_url)

tree = html.fromstring(result.text)

result = session_requests.post(login_url, payload, headers=dict(refer=login_url))

print(result)

pages = session_requests.get("https://badoo.com/profile/0626224514")#, params=dict(query="web scraping",page=2)))


#pages = requests.get("https://badoo.com/profile/0626231310", params=dict(query="web scraping",page=2))

print(pages.text)


print(pages.status_code)
print(pages.headers.get("content-type","unknown"))

soup = BeautifulSoup(pages.text,"html.parser")
links = soup.find_all("Wants")

print(links)
