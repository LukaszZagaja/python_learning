def matryoshka(doll):
    if doll == 1:
        print(f'All dolls were opened')
    else:
        matryoshka(doll-1)


matryoshka(10)