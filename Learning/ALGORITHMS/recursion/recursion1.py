def matryoshka(doll):
    if doll == 1:
        print(f'All dolls were opened')
    else:
        matryoshka(doll-1)


matryoshka(10)

def recursiveMethod(n):
    if n<1:
        print('n is smaller than 1')
    else:
        #print(n)
        recursiveMethod(n-1)
        print(n)

recursiveMethod(5)
