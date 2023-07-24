import time

t1 = time.time()
a = 0

while (time.time() - t1) < (60):
    a += 1
print(a)
print(time.time()-t1)