import requests
import yaml
from tqdm import tqdm
import json
import threading

url = "https://pan.yukaidi.com/api/v3/share?page={num}&order_by=created_at&order=DESC"
headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
  "Cookie": "Hm_lvt_0e15ed3c52b19d72392287f62ffca41a=1712064085; _pk_id.1.82fe=377b882f579a64b9.1712064086.; sl-session=yiIdLJHzHGYIUII/jpIqFw==; _clck=ejutpp%7C2%7Cfkx%7C0%7C1553; _pk_ses.1.82fe=1; Hm_lpvt_0e15ed3c52b19d72392287f62ffca41a=1713093619; cloudreve-session=MTcxMzA5MzYxOHxOd3dBTkU5SVJsWlRRamRaU2tsSVZWUk1XVmhIU0VWRFExaE5TVUZXUlRSWVNrRlFUamRZV2s5V1NWSlZWazlPU2pNMlVsUlZTVUU9fMygSmvUmFWN84Pvr7uMRPAlYGe0u1MlPxfqhCw3AgbZ",
  "Referer": "https://pan.yukaidi.com/home?path=%2Fnokidsnocry%2Flaw",
  "Origin": "https://pan.yukaidi.com",
  "Content-Length": "101",
  "Content-Type": "application/json",
  "Sec-Fetch-Site": "same-origin",
  "Dnt": "1",
  "Sec-Ch-Ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
  "Sec-Ch-Ua-Mobile": "?0",
  "Sec-Ch-Ua-Platform": "Windows",
  "Sec-Fetch-Dest": "empty",
  "Sec-Fetch-Mode": "cors",
}
data = {
  "is_dir": False,
  "password": "",
  "downloads": -1,
  "expire": 86400,
  "score": 0,
  "preview": False
}
header = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
  "Cookie": "Hm_lvt_0e15ed3c52b19d72392287f62ffca41a=1712064085; _pk_id.1.82fe=377b882f579a64b9.1712064086.; sl-session=yiIdLJHzHGYIUII/jpIqFw==; _clck=ejutpp%7C2%7Cfkx%7C0%7C1553; _pk_ses.1.82fe=1; Hm_lpvt_0e15ed3c52b19d72392287f62ffca41a=1713093619; cloudreve-session=MTcxMzA5MzYxOHxOd3dBTkU5SVJsWlRRamRaU2tsSVZWUk1XVmhIU0VWRFExaE5TVUZXUlRSWVNrRlFUamRZV2s5V1NWSlZWazlPU2pNMlVsUlZTVUU9fMygSmvUmFWN84Pvr7uMRPAlYGe0u1MlPxfqhCw3AgbZ",
}


uploaded_files = []
def send_request(uploaded_files, url):
  r = requests.get(url=url, headers=header)
  res = r.json()["data"]["items"]
  for item in res:
    data = {
      "file_name": item["source"]["name"],
      "file_share_id": item["key"],
    }
    uploaded_files.append(data)
  
threads = []

for n in range(70, 91):
  url = url.format(num=n)
  thread = threading.Thread(target=send_request, args=(uploaded_files, url,))
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join()

with open("newer_material.yaml", "a", encoding="utf-8") as f3:
  yaml.dump(uploaded_files, f3, default_flow_style=False, sort_keys=False, allow_unicode=True, width=500)
    
'''
with open("new_material.yaml", "r", encoding="utf-8") as f1:
  material_list = yaml.safe_load(f1)

result_list = material_list

for index, item in tqdm(enumerate(material_list)):
  file_id = item["file_url"].split("/")[-1]
  data["id"] = file_id
  payload = json.dumps(data)
  r = requests.post(url=url, headers=headers, data=payload)
  res = r.json()
  if res["code"] == 0:
    share_url = res["data"]
    result_list[index]["file_url"] = share_url
  else:
    print(index, item)

  
  
with open("newer_material.yaml", "a", encoding="utf-8") as f3:
  yaml.dump(result_list, f3, default_flow_style=False, sort_keys=False, allow_unicode=True, width=500)
'''
