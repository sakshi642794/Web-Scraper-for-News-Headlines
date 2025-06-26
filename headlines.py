import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.com/news"
HEADERS = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(response.content, 'html.parser')

headlines = []
for tag in soup.find_all(['h2', 'h3']):
    text = tag.get_text(strip=True)
    if text and text not in headlines:
        headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as file:
    for line in headlines:
        file.write(line + "\n")

print("Headlines saved to headlines.txt")
