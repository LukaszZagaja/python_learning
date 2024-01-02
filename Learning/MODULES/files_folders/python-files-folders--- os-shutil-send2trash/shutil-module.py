import shutil
import os

try:
    shutil.move('practice.txt', 'C:\\Users\ja\Desktop\python-files-folders\\NewPlace')
except:
    print("There was unexpected error")
    print('\n')
else:
    print("File moved succesfully")
    print('\n')

print(os.listdir('C:\\Users\ja\Desktop\python-files-folders'))
print('\n\n')
print("NewPlace folder content")
print(os.listdir('C:\\Users\ja\Desktop\python-files-folders\\NewPlace'))
print('\n')