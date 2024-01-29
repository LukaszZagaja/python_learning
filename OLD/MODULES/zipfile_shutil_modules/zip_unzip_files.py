import shutil
import zipfile

f = open('fileone.txt', 'w+')
f.write('ONE FILE')
f.close()
f = open('filetwo.txt', 'w+')
f.write('TWO FILE')
f.close()

# ZIPPING FILES
comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('fileone.txt', compress_type = zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type = zipfile.ZIP_DEFLATED)
comp_file.close()

# UNZIPPING FILES
zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')



# ZIPPING WHOLE FOLDERS
dir_to_zip = 'HERE IS WHOLE LINK C:\\Users\\' #dont want to post whole on GitHub
output_filename = 'example' # It is just a name of zipped folder that will be created
shutil.make_archive(output_filename, 'zip', dir_to_zip)

# UNZIPPING WHOLE FOLDERS
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')