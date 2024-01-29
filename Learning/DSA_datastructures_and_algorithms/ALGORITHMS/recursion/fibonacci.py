def fibonacci(n):
    if n<0 or int(n)!=n:
        return 'Number cannot be negative/is not int'
    else:
        if n in [0,1]:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(0))