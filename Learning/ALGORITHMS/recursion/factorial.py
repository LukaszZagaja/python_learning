# factorial == silnia
def factorial(n):
    if n<0 or int(n)!=n:
        return 'Number is smaller than 0 and/or is not int'
    else:
        if n in [0,1]:
            return 1
        else:
            return n*factorial(n-1)
    
print(factorial(3))