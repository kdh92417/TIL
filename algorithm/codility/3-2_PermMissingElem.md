# 3-2 PermMissingElem

- https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

## 풀이

```python
def solution(A):
    N = len(A) + 1
    S = (N*(N+1))/2
    s = sum(A)
    return int(S-s)
```

- 수의 합을 구하는 알고리즘을 이용하여 N+1 범위의 합과 N의 합을 비교하여 missing number를 구하였다.