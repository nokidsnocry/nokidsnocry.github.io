from config import headers
import yaml
import requests
import threading

headers["Referer"] = "https://pan.yukaidi.com/shares"
headers["Cookie"] = "Hm_lvt_0e15ed3c52b19d72392287f62ffca41a=1712064085; _pk_id.1.82fe=377b882f579a64b9.1712064086.; sl-session=yiIdLJHzHGYIUII/jpIqFw==; _clck=ejutpp%7C2%7Cfkx%7C0%7C1553; _pk_ses.1.82fe=1; cloudreve-session=MTcxMzExMDM2MnxOd3dBTkU5SVJsWlRRamRaU2tsSVZWUk1XVmhIU0VWRFExaE5TVUZXUlRSWVNrRlFUamRZV2s5V1NWSlZWazlPU2pNMlVsUlZTVUU9fKAvUb4L6aoHB5qyb7YVF-VismsGbVOyjEi-PRX8EIHD; Hm_lpvt_0e15ed3c52b19d72392287f62ffca41a=1713110363; _clsk=14rldzt%7C1713110363338%7C14%7C1%7Ci.clarity.ms%2Fcollect"

delete_url = "https://pan.yukaidi.com/api/v3/share/{shared_id}"

with open("data/shared_data.yaml", "r", encoding="utf-8") as f:
  shared_data = yaml.safe_load(f)

shared_id = [item["file_share_id"] for item in shared_data]

def delete(url):
  r = requests.delete(url=url, headers=headers)
  if r.json()["code"] == 0:
    print("delete success.")
  else:
    print(r.json())

threads = []

for sid in shared_id:
  url = delete_url.format(shared_id=sid)
  r = requests.delete(url=url, headers=headers)
  if r.json()["code"] == 0:
    print("delete success.")
  else:
    print(r.json())



