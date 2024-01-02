print('This program will count uneven numbers from range given by user')
range_bottom = int(input('Give starting number: '))
range_top = int(input('Give ending number: '))
sum_uneven = 0


for x in range(range_bottom, range_top):
    if x%2 != 0:
        sum_uneven += x
    else:
        continue
    
print('Sum of uneven numbers from given range is: ', sum_uneven)
