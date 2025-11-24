import os 
#  Select the  directory you want to list
directory_path = '/'
# Use the os module to list all files and directories
contents = os.listdir(directory_path)
# print  the contents of the directory
for item in contents:
    print (item)