import random

def random_number(lower, higher, times):
    for i in range(times):
        yield random.randint(lower, higher)

low = int(input(" From what number (eg: 0) you want your pseudorandom numbers to start: "))
high = int(input(" On what number (eg: 10) you want your pseudorandom numbers to end: "))
number = int(input(" How many numbers you want to create: "))

for num in random_number(low, high, number):
    print(num)
    