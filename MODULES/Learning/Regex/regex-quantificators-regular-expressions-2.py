import re

text = 'My phone number is 408-555-1234'
phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d', text)
print('\n\n')
print(phone)

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print('\n\n' , phone)


phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print('\n\nWITH PATTERN:\n' , results)
print(results.group())
print(results.group(1)) #STARTS FROM 1, NOT 0 LIKE EVERYWHERE