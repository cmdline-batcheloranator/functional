days = {
    'mon': 0,
    'tue': 0,
    'fri': 0,
    'sat': 0,
    'sun': 0
}

x = list(days.keys())
y = list(days.values())

def iterPrint(x, y):
    if not any((x, y)):
        return 0
    print(f"{x[0]}: {y[0]}")
    return iterPrint(x[1:], y[1:])

iterPrint(x, y)
