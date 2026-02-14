import os
import shutil
from time import time
from random import seed, randint, randbytes

path = input("Full Test Path: ")
if not path.startswith("/"):
    print("Must be full path.")
    exit()

seed(0)
if "FSTest" in os.listdir(path):
    shutil.rmtree(path + "/FSTest")
os.mkdir(path + "/FSTest")

totcre = 0
totread = 0
totalloc = 0
totwrite = 0
i = 0

try:
    while True:
        tmpcre = time()
        c = open(path + "/FSTest/" + hex(i)[2:], "wb+")
        totcre += time() - tmpcre
        size = randint(1, 2097152)
        data = randbytes(size)
        tmpalloc = time()
        c.truncate(size)
        c.flush()
        os.fsync(c.fileno())
        totalloc += time() - tmpalloc
        c.seek(0)
        tmpwrite = time()
        c.write(data)
        c.flush()
        os.fsync(c.fileno())
        totwrite += time() - tmpwrite
        c.seek(0)
        tmpread = time()
        d = c.read()
        totread += time() - tmpread
        c.close()
        if d != data:
            print(f"Error on file: {hex(i)[2:]}   ")
        if i % 100 == 0:
            print(f"Create Time: {totcre:.2f} {totcre/(i+1):.5f}, Read Time: {totread:.2f} {totread/(i+1):.5f}, Allocation Time: {totalloc:.2f} {totalloc/(i+1):.5f}, Write Time: {totwrite:.2f} {totwrite/(i+1):.5f}, Files: {i + 1}   ", end="\r")
        i += 1
except (Exception,KeyboardInterrupt) as e:
    try:
        c.close()
    except NameError:
        pass
    print(e)
    print(f"Create Time: {totcre:.2f} {totcre/(i+1):.5f}, Read Time: {totread:.2f} {totread/(i+1):.5f}, Allocation Time: {totalloc:.2f} {totalloc/(i+1):.5f}, Write Time: {totwrite:.2f} {totwrite/(i+1):.5f}, Files: {i + 1}   ")

input("Unmount and Remount: ")

seed(0)
for i in sorted([int(i, 16) for i in os.listdir(path + "/FSTest/")]):
    i = hex(i)[2:]
    size = randint(1, 2097152)
    data = randbytes(size)
    if os.path.getsize(path + "/FSTest/" + i) == size:
        c = open(path + "/FSTest/" + i, "rb")
        d = c.read()
        c.close()
        if d != data:
            print(f"Error on file: {i}   ")
    if int(i, 16) % 100 == 0:
        print(f"Double Checking: {int(i, 16) + 1}   ", end="\r")
print(f"Double Checking: {int(i, 16) + 1}   ")
shutil.rmtree(path + "/FSTest")
