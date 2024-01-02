# GOAL: Get all books where rating is equal 2 stars 

import requests
import bs4

# http://books.toscrape.com/catalogue/page-1.html
base = 'http://books.toscrape.com/catalogue/page-{}.html'

##     request = requests.get(base.format(1))
##     soup = bs4.BeautifulSoup(request.text, 'lxml') 
##     print(len(soup.select('.product_pod')))
##     products = soup.select('.product_pod')
##     example = products[0]
##     print([] == example.select('.star-rating.Two')) # need to write down a dot ('.') instead of (space)
##     print(example.select('a')[1]['title'])

# Checking if something is 2 star -> name.select('.star-rating.NUMBER')
# To grab the title -> name.select('a')[1]['title'] 

two_star_titles = []

for n in range(1,51):
    scrape = base.format(n)
    req = requests.get(scrape)
    
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two')) != 0: # if book rating equals 2 then len equals 1. Checks if the list is not empty 
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

#print(two_star_titles)
f = open('two star titles.txt', 'w')
for title in two_star_titles:
    f.write(str(title))
    f.write('\n')
f.close()
