import os
import shutil
from time import time
from random import seed, randint, randbytes

seed(0)
if "FSTest" in os.listdir():
    shutil.rmtree("FSTest")
os.mkdir("FSTest")

totcre = 0
totread = 0
totwrite = 0
i = 0

try:
    while True:
        tmpcre = time()
        c = open("FSTest/" + hex(i)[2:], "wb+")
        totcre += time() - tmpcre
        data = randbytes(randint(1, 2097152))#67108864))
        tmpwrite = time()
        c.write(data)
        c.flush()
        totwrite += time() - tmpwrite
        c.seek(0)
        tmpread = time()
        d = c.read()
        totread += time() - tmpread
        if d != data:
            print(f"Error on file: {i}   ")
        if i % 100 == 0:
            print(f"Create Time: {totcre}, Read Time: {totread}, Write Time: {totwrite}, Files: {i + 1}   ", end="\r")
        i += 1
except Exception as e:
    print(e)
    print(f"Create Time: {totcre}, Read Time: {totread}, Write Time: {totwrite}, Files: {i + 1}   ")
