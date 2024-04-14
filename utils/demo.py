import yaml

with open("newer_material.yaml", "r", encoding="utf-8") as f:
  uploaded_files = yaml.safe_load(f)

name_list = [item["file_name"] for item in uploaded_files]
print(len(name_list))
name_set = list(set(name_list))
print(len(name_set))
