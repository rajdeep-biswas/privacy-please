from os import listdir, remove

folders = ['uploads/', 'put_contents_here/', 'zipped/']

for folder in folders:
    files = listdir(folder)
    for file in files:
        remove(folder + file)
