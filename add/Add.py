lst = [1, 2, 3]

def add(lst):
    if not lst:
        return 0
    return lst[0] + add(lst[1:])

print(add(lst))
