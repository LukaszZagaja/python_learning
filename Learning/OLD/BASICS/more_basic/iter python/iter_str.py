s = "string_to_iterate"

s_iter = iter(s)

for char in range(len(s)):
    print(next(s_iter))