![title](https://github.com/cmdline-batcheloranator/recursion/blob/master/img/infinite.png)


# It's function time, fuck loops

everything functional

## These are all different ways of pushing 500 intergers to a list

list.py:

```python
x = list(range(500))
```

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
x =  []

for i in range(500): 
     i += 1
     x.append(i)
```

recursion.py:

```python
x =  []

def recurse(i=0):
    if i == 500:
        return 0
    recurse(i+1)
    return x.append(i)

recurse()
```

## Look at their speeds 

![speeds](https://github.com/cmdline-batcheloranator/recursion/blob/master/img/speed.png)


## Orders of speeds

1. list.py:

`1.216e-05`

2. listComp.py:  

` 2.503e-05`

3. map.py:       

` 5.364e-05`

4. loop.py:      

` 1.622e-05`

5. recursion.py  

` 3.379e-04`

## % and ratio comparison of speeds

list.py is:

- 205.8% or ~2:1, faster than listComp.py
- 441.1% or ~5:1, faster than map.py
- 788.2% or ~8:1, faster than loop.py
- 2779%  or ~28:1, faster than recursion.py

listComp.py is:

- 214.3% or ~2:1, faster than map.py
- 382.9% or ~4:1, faster than loop.py
- 1400% or 14:1, faster than recursion.py

map.py is:

- 178.7% or ~2:1, faster than loop.py
- 629.9% or ~7:1, faster than recursion.py

loop.py is:
- 352.6% or ~4:1, faster than recursion.py

## Conclusion

- `list()` and `listComprehension` come first in speed
- no surprise, they are specific to this kind of scenario

- `map()` or `listComprehension` can do everything else.

