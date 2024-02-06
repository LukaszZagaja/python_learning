from math import sqrt

def prime(num):
    if 1>=num:
        return False
    for i in range(2, sqrt(num)):
        if num%i==0:
            return False
    return True