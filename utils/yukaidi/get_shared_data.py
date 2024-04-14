import requests
import yaml
from tqdm import tqdm
import json
import threading
from config import headers

url = "https://pan.yukaidi.com/api/v3/share?page={num}&order_by=created_at&order=DESC"
pages = 90
shared_data = []
threads = []

def send_request(shared_data, url):
  r = requests.get(url=url, headers=headers)
  res = r.json()["data"]["items"]
  for item in res:
    data = {
      "file_name": item["source"]["name"],
      "file_share_id": item["key"],
    }
    uploaded_files.append(data)


for i in range(Math.floor(pages / 10)):
  for n in range(i*10+1, (i+1)*10+1):
    url = url.format(num=n)
    thread = threading.Thread(target=send_request, args=(shared_data, url,))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

  with open("shared_data.yaml", "a", encoding="utf-8") as f:
    yaml.dump(shared_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True, width=500)

  threads = []
    
