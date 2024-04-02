import requests
from bs4 import BeautifulSoup as bs
import lxml
from tqdm import tqdm
import threading
import time

url = "http://127.0.0.1:4000"

r = requests.get(url=url)
content = r.text

soup = bs(content, "lxml")
urls = soup.find_all(class_="urls")

url_list = []

for url in urls:
  link = url.a["href"]
  url_list.append(link)
  
  
def test_url(url):
  r = requests.get(url)
  if r.status_code == 404:
    print(url)

for url in tqdm(url_list):
  time.sleep(0.1)
  thread = threading.Thread(target=test_url, args=(url,))
  thread.start()
