import requests
import bs4

request = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(request.text, 'lxml')

#first_item = soup.select('.vector-toc-text')[0]
#print(first_item.text)
#print('\n')

for item in soup.select('.vector-toc-text'):  # I dont really know how to pick only div without nested span (only text without numbers)
    print(item.text)