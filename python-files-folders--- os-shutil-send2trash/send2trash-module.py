import shutil
import os
import send2trash

try:
    shutil.move('C:\\Users\ja\Desktop\python-files-folders\\NewPlace\practice.txt', os.getcwd())
except:
    print("There was unexpected error")
    print('\n')
else:
    print("File moved succesfully")
    print('\n')

send2trash.send2trash('practice.txt')