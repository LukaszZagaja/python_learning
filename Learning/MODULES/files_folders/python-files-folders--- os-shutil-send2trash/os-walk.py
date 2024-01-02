import os

file_path = 'C:\\Users\\ja\\Desktop\\python-files-folders\\Example_Top_Level'

for folder, sub_folders, files in os.walk(file_path):
    print(f"Currently looking at {folder}")
    print("\n")
    print("The subfolders are: ")
    for sub_fold in sub_folders:
        print(f"\t Subfolder: {sub_fold}")
    
    print("\n")
    print("The files are: ")
    for f in files:
        print(f"\t File: {f}")
    
    print("\n")