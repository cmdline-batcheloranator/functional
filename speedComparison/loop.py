import time  

s = time.time()

i = 0
x =  []

for i in range(500): 
     i += 1
     x.append(i)

e = time.time() - s

print(round(e, 8))
