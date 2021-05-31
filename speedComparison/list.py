import time

s =  time.time()

x = list(range(500))

e = time.time()  - s 

print(round(e, 8))
