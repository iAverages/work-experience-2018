#Glob Test2
import glob
import os

for root, dirs, files in os.walk("Z:\\", topdown=False):
    for name in files:
        fullname = os.path.join(root, name)

        if name.endswith("desktop.ini"):
            os.remove(fullname)
            print("Deleted", os.path.join(root, name))

        if name.startswith("~$"):
            os.remove(fullname)
            print("Deleted", os.path.join(root, name))            

        

