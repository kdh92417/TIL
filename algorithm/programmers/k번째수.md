# K번째 수(level 1)

## 문제

- [프로그래머스 level - K번째 수](https://programmers.co.kr/learn/courses/30/lessons/42748)

<br>

## Code

### 일반적인 풀이

```python
def solution(array, commands):
    answer = []
    for command in commands:
        new_list = sorted(array[command[0] - 1:command[1]])
        answer.append(new_list[command[-1] - 1])

    return answer
```

<br>

### List Comprehension을 이용한 풀이

```python
def solution(array, commands):
    return [sorted(array[x[0]-1:x[1]])[x[2]-1] for x in commands]
```
