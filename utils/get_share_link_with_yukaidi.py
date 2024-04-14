import requests
import yaml
from tqdm import tqdm
import json

url = "https://pan.yukaidi.com/api/v3/share"
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


with open("newer_material.yaml", "r", encoding="utf-8") as f1:
  uploaded_list = yaml.safe_load(f1)

name_list = [item["file_name"] for item in uploaded_list]

with open("id_list.yaml", "r", encoding="utf-8") as f2:
  material_list = yaml.safe_load(f2)

with open("new_material.yaml", "r", encoding="utf-8") as f3:
  result_list = yaml.safe_load(f3)

for index, item in enumerate(material_list):
  if item["file_name"] not in name_list:
    file_id = item["file_id"]
    data["id"] = file_id
    payload = json.dumps(data)
    r = requests.post(url=url, headers=headers, data=payload)
    res = r.json()
    if res["code"] == 0:
      print("success:" + item["file_name"])
    else:
      print("fail:" + item["file_name"])

  
with open("newer_material.yaml", "a", encoding="utf-8") as f3:
  yaml.dump(result_list, f3, default_flow_style=False, sort_keys=False, allow_unicode=True, width=500)
'''
