def sito(liczba):
    numbers = [True for _ in range(liczba)]
    primes = []
    for i in range(liczba):
        if i <= 1:
            numbers[i] = False
        else:
            if numbers[i]: # if numbers[i]==true
                primes.append(i)
                for j in range(i, len(numbers), i):  # if i=2=true then 4,6,8 etc are deemed false
                    numbers[j] = False
    return primes

print(sito(25))