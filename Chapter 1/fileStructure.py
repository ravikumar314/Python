import os

# direct to list
directory_path = '/Users/vermarap/Python'

# list all files and directories in specified path
contents = os.listdir(directory_path)

#print each file and directory name
for item in contents:
    print(item)