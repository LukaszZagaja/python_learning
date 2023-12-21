import re

print('\n', re.search(r'cat|dog' , "The cat is here"))

# Wildcard operator

print('\n', re.findall(r'at', "The cat in the hat sat there.")) #NORMAL
print('\n', re.findall(r'.at', "The cat in the hat sat there.")) #WILDCARD


#Starts/ends with
print('\n\n', re.findall(r'^\d', '1 is a number'))
print(re.findall(r'^\d', 'The 1 is a number'))
print(re.findall(r'\d$', '1 is a number'))
print(re.findall(r'\d$', 'Number is 1'))




# Exclusion

phrase = 'there are 3 numbers 34 inside 5 this sentence'
pattern = r'[^\d]+'

print('\n\n')
print(re.findall(pattern, phrase))



test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
clean = re.findall(r'[^!.? ]+', test_phrase)
print(' '.join(clean))


 # Inclusion 

text = 'Only find the hypen-words in this sentence. But you do not know how long-ish they are'
pattern = r'[\w]+-[\w]+'
print('\n\n')
print(re.findall(pattern, text)) 