s = 'hello world'
s1 = 'HELLO WORLD'

print('\n')
print(s.capitalize()) # cappitalizes only first char of first word
print(s.upper())
print(s1.lower)
print(s.count('l')) # counts every given char 
print(s.find('o')) # returns index where it finds the first char
print('\n')


# Formatting methods 
# s.center(20, '-') # makes basically ----------hello world---------
print('hello\thi') # \t means tabulator (4 spaces)
print('\n\n')

s = 'hello'
print(s.isalnum()) # checks if string is alphanumeric
print(s.isalpha()) # checks if string is only using alphabet (a-z)
print(s.islower())
print(s.isupper())
print(s.isspace()) # checks if there is space in string
print(s.istitle()) # to return true string must be looking like: 'Hello World It Is Great Day Today' 
print(s.endswith('o'))
print('\n')

print(s.split('e')) # returns the result in a list, case is 'deleted'
print(s.partition('e')) # occurs only on the first case, returns what was before case, case, and everything that was after. Also list