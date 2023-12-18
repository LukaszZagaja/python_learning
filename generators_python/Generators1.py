def generator_squares(times):
    for i in range(times):
        yield i**2

time = int(input("How many squared numbers (excluding 0): "))

for x in generator_squares(time+1):
    print(x)
    