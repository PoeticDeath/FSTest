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
totalloc = 0
totwrite = 0
i = 0

try:
    while True:
        tmpcre = time()
        c = open("FSTest/" + hex(i)[2:], "wb+")
        totcre += time() - tmpcre
        size = randint(1, 2097152)
        data = randbytes(size)
        tmpalloc = time()
        c.write(bytes(size))
        c.flush()
        totalloc += time() - tmpalloc
        c.seek(0)
        tmpwrite = time()
        c.write(data)
        c.flush()
        totwrite += time() - tmpwrite
        c.seek(0)
        tmpread = time()
        d = c.read()
        totread += time() - tmpread
        if d != data:
            print(f"Error on file: {hex(i)[2:]}   ")
        if i % 100 == 0:
            print(f"Create Time: {totcre:.2f} {totcre/(i+1):.5f}, Read Time: {totread:.2f} {totread/(i+1):.5f}, Allocation Time: {totalloc-totwrite:.2f} {(totalloc-totwrite)/(i+1):.5f}, Write Time: {totwrite:.2f} {totwrite/(i+1):.5f}, Files: {i + 1}   ", end="\r")
        i += 1
except Exception as e:
    print(e)
    print(f"Create Time: {totcre:.2f} {totcre/(i+1):.5f}, Read Time: {totread:.2f} {totread/(i+1):.5f}, Allocation Time: {totalloc-totwrite:.2f} {(totalloc-totwrite)/(i+1):.5f}, Write Time: {totwrite:.2f} {totwrite/(i+1):.5f}, Files: {i + 1}   ")

seed(0)
for i in os.listdir("FSTest/"):
    size = randint(1, 2097152)
    data = randbytes(size)
    if os.path.getsize("FSTest/" + i) == size:
        c = open("FSTest/" + i, "rb").read()
        if c != data:
            print(f"Error on file: {i}   ")
    if int(i, 16) % 100 == 0:
        print(f"Double Checking: {int(i, 16)}   ", end="\r")
print(f"Double Checking: {int(i, 16) + 1}   ")
shutil.rmtree("FSTest")
