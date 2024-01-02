import requests
import bs4

result = requests.get('http://example.com/')
#print(type(result)) # Checks if site responds 
# print(result.text) Writes down whole html code of site as string

soup = bs4.BeautifulSoup(result.text, 'lxml')
#print(soup) # prints down html code down like in editor 

print('\n')
print(soup.select('title')) # what you want to grab needs to be inside those quotation marks (i.e. title, h1, p, a, span, etc...)
                            # also it gives back a list because there can be more than 1 instation of given html tag

print(soup.select('title')[0]) # without square bracket
print(soup.select('title')[0].getText()) # clear text without tags or bracket 
print('\n\n')


site_paragraphs = soup.select('p')
print(site_paragraphs)
print(site_paragraphs[0])
print(type(site_paragraphs[0])) # this is not a string, its special bs4 type 

string_ver = site_paragraphs[0].getText() # this changes it to string