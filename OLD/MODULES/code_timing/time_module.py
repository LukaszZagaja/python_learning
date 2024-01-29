import time
def func_1(n):
    return[str(num) for num in range(n)]

def func_2(n):
    return list(map(str, range(n)))

print('\n\n')

# ----- FUNCTION 2 -----------------------------------------------------
# TIME BEFORE
start_time = time.time()

# CODE
result = func_1(1000000)

# END TIME
end_time = time.time()

# ELAPSED TIME
elapsed_time = end_time - start_time
print("Function 1 took ", elapsed_time)



# ----- FUNCTION 2 -----------------------------------------------------

# TIME BEFORE
start_time = time.time()

# CODE
result = func_2(1000000)

# END TIME
end_time = time.time()

# ELAPSED TIME
elapsed_time = end_time - start_time
print("Function 2 took ", elapsed_time)