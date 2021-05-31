![title](https://github.com/cmdline-batcheloranator/recursion/blob/master/img/infinite.png)


# It's recursion time, fuck loops

All things recusion and functional


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

## % Comparison of speeds

list.py is:

- 205.8% faster than listComp.py
- 441.1% faster than map.py  
- 788.2% faster than loop.py
- 2779% faster than recursion.py  


listComp.py is:

- 214.3% faster than map.py
- 382.9% faster than loop.py 
- 1400% faster than recursion.py

map.py is:

- 178.7% faster than loop.py  
- 629.9% faster than recursion.py

loop.py is:

- 352.6% faster than recursion.py
