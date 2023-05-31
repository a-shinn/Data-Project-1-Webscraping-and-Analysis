import pandas as pd
import bs4 as bs
import requests

webpage = requests.get('https://www.animanga.com/scripts/textesgb/eva1.html')
soup = bs.BeautifulSoup(webpage.text, 'html.parser')
text = soup.get_text()

character_lines: {}

for row in text.splitlines():
    print(row)