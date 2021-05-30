import time  

s = time.time()

i = 0
lst =  []

for i in range(500): 
     i += 1
     lst.append(i)

e = time.time() - s

print(round(e, 8))
