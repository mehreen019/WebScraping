from bs4 import BeautifulSoup
import requests
import time
import json

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url = "https://www.daraz.com.bd/catalog/?page=1&q=sunscreen&spm=a2a0e.tm80335411.search.d_go"
response = requests.get(url, headers = headers)
soup = BeautifulSoup(response.text, 'lxml')

script = soup.find('script', id="group_umid")
if script:
    try:
        # Print the raw script content for debugging
        print("Raw script content:", script.string)
        data = json.loads(script.string)
        print(data.keys())
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
else:
    print("Script tag with id 'group_umid' not found")



"""
for x in range(1,2):
    url = "https://www.daraz.com.bd/catalog/?page=1&q=sunscreen&spm=a2a0e.tm80335411.search.d_go"
    response = requests.get(url, headers = headers)
    soup = BeautifulSoup(response.text, 'lxml')
    products = soup.find('div', class_ = "ant-row FrEdP css-1bkhbmc app")
    print(soup.text)

"""