import yaml
from urllib.parse import unquote

with open('material.yaml', 'r', encoding='utf-8') as f:
  data = yaml.safe_load(f)

for file in data['content']:
  unquoted_url = unquote(file['urls'][0]['book_url'])
  file['urls'][0]['book_url'] = unquoted_url
  file['url-path'] = unquoted_url.split('material')[-1]

with open('material_done.yaml', 'a', encoding='utf-8') as f1:
  yaml.dump(data, f1, allow_unicode=True)
