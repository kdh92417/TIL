# Array Manipulation

- https://www.hackerrank.com/challenges/crush/problem

## Solve

### 시간초과된 풀이

```python
def arrayManipulation(n, queries):
    # Write your code here
    sum_list = [0] * (n + 1)

    for i in queries:
        for j in range(i[0], i[1] + 1):
            sum_list[j] += i[2]
    
    return max(sum_list)
```

- 중첩반복문으로 시간 복잡도 O(n * m) => O(n<sup>2</sup>)으로 시간초과가 된 풀이이다.

<br>

### prefix sum(부분합)을 이용한 풀이

```python
def arrayManipulation(n, queries):
    # Write your code here
    # 부분합 리스트
    k_list = [0] * (n + 1)

    # 리턴할 가장 높은 값
    max_val = 0

    # 부분합 리스트 업데이트
    for s, e, k in queries:
        k_list[s] += k
        if e + 1 <= n:
            k_list[e +1] -= k
    
    # max_val과 비교하기 위한 변수 설정
    result = k_list[0]

    # 부분합의 누적합을 구하면서 최대 값을 구한다.
    for i in range(1, n+1):
        result += k_list[i]
        if result > max_val:
            max_val = result
            
    return max_val
```

n개의 요소를 일일이 더해가면서 합을 구하는 것이 아니라 부분합 알고리즘을 이용하여 O(n)의 시간복잡도로 풀이한 코드이다.