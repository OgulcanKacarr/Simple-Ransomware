from cryptography.fernet import Fernet
import os

secret_key = input("Enter key: ")

file_list = []
for files in os.listdir():
    if files == "ransomware.py" or files == "de-ransomware.py":
        continue
    if os.path.isfile(files):
        file_list.append(files)

for file in file_list:
    with open(file,"rb") as the_file:
        contents = the_file.read()
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file,"wb") as the_file:
        the_file.write(contents_decrypted)