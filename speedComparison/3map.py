import time 

s = time.time()

x = list(map(lambda x: x+1, range(500)))

e = time.time()  - s

print(round(e, 8))
