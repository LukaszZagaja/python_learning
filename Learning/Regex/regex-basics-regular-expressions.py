import re

print('\n\n')
text = "The agent's phone number is 408-555-1234. Call soon!"
print('phone' in text)

pattern = 'phone'
print(re.search(pattern, text))
pattern = 'NOT IN TEXT'
print(re.search(pattern, text))
print('\n')


pattern = 'phone'
match = re.search(pattern, text)
print("Span of match")
print(match.span())

print('Start of match')
print(match.start())

print('End of match')
print(match.end())
print('\n\n')

text = 'My phone once, my phone twice'
print(text)
match = re.search(pattern, text)


print("Return only the first match ")
print(match.span())
print('\n')

print(text)
matches = re.findall(pattern, text)
print(matches)
print("How many matches: ")
print(len(matches))


print('\n\n For loop: \n')
for match in re.finditer('phone', text):
    print(match.group() , " " , match.span())

