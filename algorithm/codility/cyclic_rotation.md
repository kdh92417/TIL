# CyclicRotation

```python
def solution(A, K):
    # write your code in Python 3.6
    answer = [0] * len(A)
    
    for i, v in enumerate(A):
        idx = (i + K) % len(A)
        answer[idx] = v
    return answer
```

- K번의 이동을 한번씩하는 것이 아니라 변경된 최종 인덱스를 계산하여 최종 회전된 배열을 반환하는 풀이이다.