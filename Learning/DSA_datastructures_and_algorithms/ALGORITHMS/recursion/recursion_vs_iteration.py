# Recursion 
def powerOfTwoRec(n):
    if n==0:
        return 1
    else:
        power = powerOfTwoRec(n-1)
        return power*2
    
# Iterative
def powerOfTwoIter(n):
    i=0
    power=1
    while i<n:
        power=power*2
        i=i+1
    return power

print(f'10th power of 2 using Recursion: {powerOfTwoRec(10)}')
print(f'10th power of 2 using Iterative: {powerOfTwoIter(10)}')
