"""
更新有效的封面链接
"""

import json
import yaml
from tqdm import tqdm

base_file = "data/material.json"
cover_file = "data/cover_url.yml"
output_file = "data/output.json"

def repalce_cover_url():
    count = 0
    with open(base_file, "r", encoding="utf-8") as f:
        base_data = json.load(f)
    with open(cover_file, "r", encoding="utf-8") as f:
        cover_data = yaml.safe_load(f)
    for cover_item in tqdm(cover_data):
        cover_name = cover_item["cover_name"].rpartition(".")[0]
        for base_item in base_data["content"]:
            if base_item["name"] == cover_name:
                base_item["cover_url"] = cover_item["cover_src"]
                count += 1
                break
            else:
                continue
    print(f"新增{count}个文件。")
        
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(base_data, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    repalce_cover_url()