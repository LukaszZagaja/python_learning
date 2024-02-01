def euclides(a,b):
    while a != b:
        if a > b:
            a-=b
        elif b > a:
            b-=a
    return a # a is equal to b so you can return which one you want 

print(euclides(8,12))
