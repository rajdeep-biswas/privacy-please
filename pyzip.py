import pyzipper
import string 
import random 
from os import listdir
from datetime import datetime

out_folder = "zipped/"

pass_len = 25

password = bytes(''.join(random.choices(string.ascii_uppercase + string.digits, k = pass_len)), encoding='utf-8')
timestamp = datetime.timestamp(datetime.now())
with pyzipper.AESZipFile(out_folder + str(timestamp) +'.zip',
                         'w',
                         compression=pyzipper.ZIP_LZMA,
                         encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword(password)
    zf.setencryption(pyzipper.WZ_AES, nbits=256)
    for file in listdir("put_contents_here/"):
        zf.write("put_contents_here/" + file)

with pyzipper.AESZipFile(out_folder + str(timestamp) +'.zip') as zf:
    zf.setpassword(password)

with open(out_folder + str(timestamp) + '-password.txt', 'w') as text:
    print(str(password).split("'")[1])
    text.write(str(password).split("'")[1])
