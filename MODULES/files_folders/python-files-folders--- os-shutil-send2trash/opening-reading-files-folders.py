import os
f = open('practice.txt', "a")
f.write("This is a test string")
f.close()

print(os.getcwd())
print("\n\n")

print(os.listdir())
print("\n")

print(os.listdir('C:\\Users'))
print("\n")
