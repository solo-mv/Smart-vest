import os
from os import path
import shutil
print(os.getcwd())

def movingfiles():
    src="/media/solomv/0A8C-3377/"
    dst="/home/solomv/Desktop/code/testtest"

    print(os.listdir(src))

    files = [i for i in os.listdir(src) if i.endswith("png") or i.endswith("jpg")  or i.endswith("jpeg") and path.isfile(path.join(src, i))]
    print(files)
    for f in files:
        shutil.move(path.join(src, f), dst)
        print(os.getcwd())

