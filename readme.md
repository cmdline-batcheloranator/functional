![title](https://github.com/cmdline-batcheloranator/recursion/blob/master/img/infinite.png)


# Its recursion time fuck loops

All things recusion and functional

---



## These are all different ways of pushing 500 intergers to a list

listComp.py:

```python
x = [i for i in range(500)]
```

map.py:

```python 
x = list(map(lambda x: x+1, range(500)))
```

loop.py:

```python
i = 0
lst =  []

for i in range(500): 
     i += 1
     lst.append(i)
```

recursion.py:

```python
lst =  []

def recurse(i=0):
    if i == 500:
        return 0
    recurse(i+1)
    return lst.append(i)

recurse()
```

## Now look at their speeds 

![speeds](https://github.com/cmdline-batcheloranator/recursion/blob/master/img/speed.png)


## Orders of speeds

1. listComp.py:   2.718e-05
2. map.py:        5.507e-05
4. loop.py:       8.512e-05
3. recursion.py   5.329e-04

## % Comparison of speeds

listComp.py is:

- 202.6% faster than map.py
- 313.2% faster than loop.py 
- 2447% faster than recursion.py

map.py is:

- 154.6% faster than loop.py  
- 967.7% faster than recursion.py

loop.py is:

- 626.1% faster than recursion.py
