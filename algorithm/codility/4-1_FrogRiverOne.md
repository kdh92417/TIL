# FrogRiverOne

## 문제

- https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

## 풀이

### Brtue Force : 시간복잡도 O(n<sup>2</sup>)

```python
def solution(X, A):
    # write your code in Python 3.6
    
    c = [True] + [False] * X

    for i, v in enumerate(A):
        c[v] = True
        if False not in c:
            return i
    return -1
```

### 합을 이용한 풀이 : 시간복잡도 O(n)

```python
def solution(X, A):
    # write your code in Python 3.6
    
    c = [0] + [0] * X
    total = 0

    for i, v in enumerate(A):
        if c[v] == 0:
            c[v] = 1
            total += 1
            if total == X:
                return i
    return -1
```