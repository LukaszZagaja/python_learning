whole = 0
amount = []
print('Adding will stop adding numbers when your whole sum is equal or bigger than 100 and then write down how many numbers were added')

while whole < 100:
    adding = int(input('Give a number: '))
    whole += adding
    amount.append(adding)
    
print('Amount of numbers added before reaching 100 is equal to: ', len(amount))