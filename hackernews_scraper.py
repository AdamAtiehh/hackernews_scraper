import requests
from bs4 import BeautifulSoup
import pprint

try:
    res = requests.get('https://news.ycombinator.com/news')
    res.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    exit()
    
soup=BeautifulSoup(res.text,'html.parser')
links=soup.select('.titleline')
votes=soup.select('.score')
#select will act as a css selector where u can select an id and class

def create_custom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        if idx >= len(votes):
            # Skip this item if there are no corresponding votes
            continue
        title = item.getText()
        href = item.find('a').get('href', None)
        points = int(votes[idx].getText().replace(' points', ''))
        hn.append({'title': title, 'link': href, 'points': points})
        hn_sorted = sorted(hn, key=lambda x: x['points'], reverse=True)
    return hn_sorted

pprint.pprint(create_custom_hn(links, votes))
