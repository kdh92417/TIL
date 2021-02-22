# 다시한번 상기시켜 볼만 한 것들

## 해당 리스트에서 홀수 인 요소들 삭제하기

- 반복문 안에서 i를 증가시키면서 요소를 삭제하면 지나치는 요소들이 생겨 홀수는 삭제시키고 i를 증가 시키지않고 짝수는 i를 증가시킨다.

```python
numbers = [1, 7, 3, 6, 5, 2, 13, 14]

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 1:
        del numbers[i]
    else:
        i += 1
```
