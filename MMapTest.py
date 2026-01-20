import mmap
from os import remove
from random import randbytes
length = 67108864
fn = "0"
data = randbytes(length)
c = open(fn, "wb+")
c.write(bytes(length))
c.flush()
d = mmap.mmap(c.fileno(), length)
d.write(data)
d.flush()
d.seek(0)
print(data == d.read())
d.close()
c.seek(0)
print(data == c.read())
c.close()
remove(fn)
