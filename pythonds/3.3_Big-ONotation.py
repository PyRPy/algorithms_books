# 3.3 Big-O Notation 
import time
a = 5 
b = 6 
c = 10 
n = 10000
start = time.time()
for i in range(n):
    for j in range(n):
        x = i * i 
        y = j * j 
        z = i * j 
end = time.time() 
print("it uses {0:0.5f} seconds to finish it".format(end - start))

for k in range(n):
    w = a*k + 45 
    v = b*b  

d = 33 
