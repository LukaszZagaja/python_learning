def euclid(a,b):
    if a != b:
        if a > b:
            return euclid(a-b, b)
        else:
            return euclid(a, b-a)
    return a # can return which one you want

print(euclid(8,28))