# OddOccurrencesInArray

- https://app.codility.com/demo/results/training8PEBSU-G7R/

## 풀이

### Counter() 함수를 이용한 풀이

```python
import collections

def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]
    c = collections.Counter(A)

    for k, v in c.items():
        if v % 2 == 1:
            return k
```

### reduce() 함수와 xor 비트연산자를 이용한 풀이

```python
from functools import reduce

def solution(A):
    # write your code in Python 3.6
    return reduce(lambda x,y:x^y , A)
```