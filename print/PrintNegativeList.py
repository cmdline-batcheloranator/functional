lst = [1, 2, 3]

def iterPrint(lst, l = len(lst)):
    i = l - 1
    if i < 0:
        return 0
    print(lst[i])
    return iterPrint(lst, i)

iterPrint(lst)
