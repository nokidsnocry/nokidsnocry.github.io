import requests
import yaml
from tqdm import tqdm
import json
from config import headers

url = "https://pan.yukaidi.com/api/v3/share"

data = {
  "is_dir": False,
  "password": "",
  "downloads": -1,
  "expire": 86400,
  "score": 0,
  "preview": False
}


with open("data/id_list.yaml", "r", encoding="utf-8") as f1:
  id_list = yaml.safe_load(f1)

with open("data/material.yaml", "r", encoding="utf-8") as f2:
  materials = yaml.safe_load(f2)

for mat in materials[:100]:
  if "ss" in mat:
    file_name = mat["name"] + "_" + str(mat["ss"]) + "." + mat["format"]
  else:
    file_name = mat["name"] + "." + mat["format"]
  for item in id_list:
    if file_name == item["file_name"]:
      file_id = item["file_id"]
      data["id"] = file_id
      payload = json.dumps(data)
      r = requests.post(url=url, headers=headers, data=payload)
      res = r.json()
      if res["code"] == 0:
        print("success:" + item["file_name"])
        mat["file_url"] = res["data"]
        mat = [mat]
        with open("data/newer_material.yaml", "a", encoding="utf-8") as f3:
          yaml.dump(mat, f3, default_flow_style=False, sort_keys=False, allow_unicode=True, width=500)
      else:
        print("fail:" + item["file_name"])
