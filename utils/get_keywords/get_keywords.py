import requests
from bs4 import BeautifulSoup as bs
import lxml
import jieba

url = 'https://nokidsnocry.github.io/'
r = requests.get(url)
content = r.text

soup = bs(content, 'lxml')
book_list = soup.find_all(class_='material-name')
book_name_list = []
for item in book_list:
    book_name = item.text
    book_name_list.append(book_name)


keywords_string = []
for each in book_name_list:
    seg = jieba.lcut(each)
    keywords_string += seg

result = {}
for ch in keywords_string:
    if ch in result:
        result[ch] += 1
    else:
        result[ch] =1

result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
print(result)
