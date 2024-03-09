import requests
from bs4 import BeautifulSoup as bs
import lxml
from tqdm import tqdm

url = "http://127.0.0.1:4000"

r = requests.get(url=url)
content = r.text

soup = bs(content, "lxml")
urls = soup.find_all(class_="urls")

for url in tqdm(urls):
  link = url.a["href"]
  r = requests.get(url=link)
  if r.status_code == 404:
    print(link)
  else:
    print(r.status_code)
  
