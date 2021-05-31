import time

s =  time.time()

x = [i for i in range(500)]

e = time.time()  - s 

print(round(e, 8))
