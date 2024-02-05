def primes(num):
    prime = []
    divider = 2
    while num != 1:
        while num % divider == 0:
            #print(divider)
            num = num//divider
            prime.append(divider)
        divider+=1
    return prime


primes(63)
