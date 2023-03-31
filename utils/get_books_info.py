import sys
import requests
import re
from bs4 import BeautifulSoup as bs
import lxml
import yaml
import time, random
import config

book_search_base_url = 'https://findbooks.eu.org/index.php?search-index-mid-2-keyword-{}-page-{}.html'
book_info_base_url = 'https://findbooks.eu.org{}'

def get_headers():
    user_agent = random.choice(config.USER_AGENT_POOL)
    headers = {
        'user-agent': user_agent
    }
    return headers


def get_book_path(keyword):
    book_path_dict = {}
    for n in range(1, 1000):
        try:
            time.sleep(1)
            url = book_search_base_url.format(keyword, n)
            r = requests.get(url, headers=get_headers())
            content = r.text

            soup = bs(content, 'lxml')
            items = soup.find('ul', class_='clearfix').find_all('a')
            pagination = soup.find('ul', class_='pagination').find_all('a')
            for item in items:
                text = item.text
                book_path = item.get('href')
                book_path_dict[text] = book_path
            if pagination and pagination[len(pagination)-1].text == "»":
                continue
            else:
                break
        except Exception as e:
            print(e)
            continue
    return book_path_dict


def get_book_info(book_path_dict):
    book_info_list = []
    for value in book_path_dict.values():
        try:
            time.sleep(1)
            book_info_url = book_info_base_url.format(value)
            r = requests.get(book_info_url, headers=get_headers())
            content = r.text

            soup = bs(content, 'lxml')
            info = soup.find('div', class_='content').text

            book_name_pattern = '【书名】：(.*?)\n'
            book_author_pattern = '【作者】：(.*?)\n'
            book_press_pattern = '【出版社】：(.*?)\n'
            book_date_pattern = '【时间】：(.*?)\n'
            book_pages_pattern = '【页数】：(.*?)\n'
            book_isbn_pattern = '【ISBN】：(.*?)\n'
            book_sscode_pattern = '【SS码】：(.*?)\n'
            book_mccode_pattern = '【秒传码】：(.*?)\n'
            book_name = re.search(book_name_pattern, info).group(1)
            book_author = re.search(book_author_pattern, info).group(1)
            book_press = re.search(book_press_pattern, info).group(1)
            book_date = re.search(book_date_pattern, info).group(1)
            book_pages = re.search(book_pages_pattern, info).group(1)
            book_isbn = re.search(book_isbn_pattern, info).group(1)
            book_sscode = re.search(book_sscode_pattern, info).group(1)
            book_mccode = re.search(book_mccode_pattern, info).group(1)

            book_name = book_name.replace(' ','-')

            info_dict = {
                "book_name": book_name,
                "book_author": book_author,
                "book_press": book_press,
                "book_date": book_date,
                "book_pages": book_pages,
                "book_isbn": book_isbn,
                "book_sscode": book_sscode,
                "book_mccode": book_mccode
            }
            book_info_list.append(info_dict)
        except Exception as e:
            print(e)
            continue
    return book_info_list
    

def write_to_file(book_info_list):
    with open('full_books_info.yaml', 'a+', encoding='utf-8') as f1:
        f1.seek(0)
        data = f1.read()
        data = yaml.safe_load(data)
        if data:
            repeat_list = []
            for info_dict in book_info_list:
                if info_dict['book_sscode'] in [item['book_sscode'] for item in data]:
                    repeat_list.append(info_dict)  
            for item in repeat_list:
                book_info_list.remove(item)
        if book_info_list:
            f1.seek(0,2)
            yaml.dump(book_info_list, f1, default_flow_style=False, sort_keys=False, allow_unicode=True, width=500) 
            with open('valid_books_info.yaml', 'a+', encoding='utf-8') as f2:
                yaml.dump(book_info_list, f2, default_flow_style=False, sort_keys=False, allow_unicode=True, width=500) 


def main():
    keyword = sys.argv[1]
    book_path_dict = get_book_path(keyword)
    book_info_list = get_book_info(book_path_dict)
    write_to_file(book_info_list)    


if __name__ == '__main__':
    main()
