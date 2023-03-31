import requests

headers = {
    'cookie': '_tokenKey=4inNM9weQVOSMnPpTd318w==.o1SQRE-fHNMkYvS9KHfape7IB-d0jZTR_DGZi4sIWeI=',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

r = requests.get('https://ap1.storj.io/new-project-dashboard', headers = headers)
content = r.text
print(content)
