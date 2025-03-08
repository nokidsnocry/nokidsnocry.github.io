"""
更新有效的文件链接
"""

import json
import yaml
import time
from tqdm import tqdm

base_file = "data/material.json"
url_file = "data/file_url.yml"
output_file = "data/output.json"

def replace_file_url():
    new_data_count = 0
    with open(base_file, "r", encoding="utf-8") as f:
        base_data = json.load(f)
    with open(url_file, "r", encoding="utf-8") as f:
        url_data = yaml.safe_load(f)
    for url_item in tqdm(url_data):
        if "_" in url_item["name"]:
            url_item_name = url_item["name"].rpartition("_")[0]
        else:
            url_item_name = url_item["name"].rpartition(".")[0]
        matched = False
        for base_item in base_data["content"]:
            if base_item["name"] == url_item_name:
                base_item["file_url"] = url_item["url"]
                matched = True
                break
            else:
                continue
        if not matched:
            new_data_count += 1
            new_data = {
                "index": 70000000 + new_data_count,
                "format": "pdf",
                "name": url_item_name,
                "type": "textbook",
                "utime": int(time.time()),
                "file_url": url_item["url"],
            }
            base_data["content"].append(new_data)
            print(url_item_name)
    print(f"新增{new_data_count}个文件。")
        
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(base_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    replace_file_url()