import time 

s = time.time()

lst =  []

def recurse(i=0):
    if i == 500:
        return 0
    recurse(i+1)
    return lst.append(i)

recurse()

e = time.time() - s

print(round(e, 8))
