days = {
    'mon': 0,
    'tue': 0,
    'fri': 0,
    'sat': 0,
    'sun': 0
}

x = list(days.keys())
y = list(days.values())

list(map(lambda r, z: print(f"{r}: {z}"), x, y))
