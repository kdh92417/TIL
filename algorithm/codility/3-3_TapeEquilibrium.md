# 3-3. TapeEquilibrium

- https://app.codility.com/demo/results/trainingMQNT46-6Y7/

## 풀이

```python
def solution(A):
    # write your code in Python 3.6
    sum_num = sum(A)
    
    left_sum = 0
    right_sum = sum_num
    min_num = None
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum -= A[i]
        m = abs(left_sum - right_sum)

        if min_num > m:
            min_num = m

    return min_num
```

- 애초에 왼쪽의 합친값과 오른쪽의 합친값을 구해두고 배열의 요소를 돌떄마다 왼쪽의 합친값과 오른쪽의 합친값을 빼고 더하면서 테이프 구간의 최솟값을 구하였다.