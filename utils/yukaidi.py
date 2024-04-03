import requests
import yaml
from tqdm import tqdm

id_list = []

root_dir = "nokidsnocry"
base_url = "https://pan.yukaidi.com/api/v3/directory"
headers = {
  "Referer": "https://pan.yukaidi.com/home?path=%2Fnokidsnocry",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
  "Cookie": "sl-session=sQW7BtJXDWarpl9IuS7+TA==; Hm_lvt_0e15ed3c52b19d72392287f62ffca41a=1712064085; _pk_id.1.82fe=377b882f579a64b9.1712064086.; _clck=ejutpp%7C2%7Cfkl%7C0%7C1553; Hm_lpvt_0e15ed3c52b19d72392287f62ffca41a=1712074851; _pk_ses.1.82fe=1; _clsk=tm0je5%7C1712074919060%7C17%7C1%7Ch.clarity.ms%2Fcollect; cloudreve-session=MTcxMjA3NDk4M3xOd3dBTkU5SVJsWlRRamRaU2tsSVZWUk1XVmhIU0VWRFExaE5TVUZXUlRSWVNrRlFUamRZV2s5V1NWSlZWazlPU2pNMlVsUlZTVUU9fLmjDMgLjX-F9kJXbKijSnRSXd5AmAIhKmrhT36CPoFK"
  }


def get_dirs():
  dirs = []
  url = base_url + "/" + root_dir
  r = requests.get(url=url, headers=headers)
  print(r.json())
  content = r.json()["data"]["objects"]
  for item in content:
    result = item["path"] + "/" + item["name"]
    dirs.append(result)
  return dirs


def get_id(dirs):
  for d in dirs:
    url = base_url + d
    r = requests.get(url=url, headers=headers)
    content = r.json()["data"]["objects"]
    for item in content:
      data = {
        "file_name": item["name"],
        "file_id": item["id"],
      }
      id_list.append(data)
  return id_list


def write_to_yaml(id_list):
  with open("id_list.yaml", 'a', encoding="utf-8") as file:
    yaml.dump(id_list, file, default_flow_style=False, sort_keys=False, allow_unicode=True, width=500)


def main():
  dirs = get_dirs()
  id_list = get_id(dirs)
  write_to_yaml(id_list)


def add_file_url():
  material_list = []
  file_base_url = "https://pan.yukaidi.com/api/v3/file/preview/"
  with open("id_list.yaml", "r", encoding="utf-8") as f1:
    id_list = yaml.safe_load(f1)
  with open("material.yaml", "r", encoding="utf-8") as f2:
    material = yaml.safe_load(f2)

  for i in tqdm(material):
    for j in id_list:
      if "ss" in i:
        file_name = i["name"] + "_" + str(i["ss"]) + "." + i["format"]
      else:
        file_name = i["name"] + "." + i["format"]
      if file_name == j["file_name"]:
        i["file_url"] = file_base_url + j["file_id"]
        material_list.append(i)
        break

  print(material_list)
  with open("new_material.yaml", "a", encoding="utf-8") as f3:
    yaml.dump(material_list, f3, default_flow_style=False, sort_keys=False, allow_unicode=True, width=500)

add_file_url()
  

  


