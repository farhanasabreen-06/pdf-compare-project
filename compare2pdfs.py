import os
import hashlib
def hash_file(file_path):
    h = hashlib.sha1()
    with open(file_path, "rb") as file:
        chunk=file.read(1024)
        while chunk:
            h.update(chunk)
            chunk=file.read(1024)
    return h.hexdigest()

base_path=os.path.join(os.getcwd(),"files")

file1=os.path.join(base_path,"PDF-1.pdf")
file2=os.path.join(base_path,"PDF-2.pdf")

hash1=hash_file(file1)
hash2=hash_file(file2)

if (hash1!=hash2):
    print("These files are not identical")
else:
    print("Files are identical")

