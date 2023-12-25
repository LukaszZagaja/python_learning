import requests
import bs4

request = requests.get('https://en.wikipedia.org/wiki/J%C3%B3zef_Pi%C5%82sudski')
soup = bs4.BeautifulSoup(request.text, 'lxml')

pilsudski = soup.select('img')[5]

pilsudski['src']
image_link = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/J%C3%B3zef_Pi%C5%82sudski_%28-1930%29.jpg/220px-J%C3%B3zef_Pi%C5%82sudski_%28-1930%29.jpg') 
                                    # this link here is link from pilsudski['src']
#print(image_link.content)
f = open('my_computer_image.jpg', 'wb')
f.write(image_link.content)
f.close()