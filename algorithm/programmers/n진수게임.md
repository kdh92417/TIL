# 2018 KAKAO BLIND RECRUITMENT - 3차 n진수 게임

- [문제](https://programmers.co.kr/learn/courses/30/lessons/17687)

## 풀이

### 통과되지 못한 나의 풀이

```python
from collections import deque

def solution(n, t, m, p):
    answer = ''
    
    i = 0
    turn = 1
    while len(answer) < t:
        
        if n == 2:
            num = bin(i)[2:]
        elif n == 8:
            num = oct(i)[2:]
        elif n == 16:
            num = hex(i)[2:]
        else:
            num = str(i)

        for s in num:
            if len(answer) == t:
                return answer
            
            if (turn - p) % m == 0:
                answer += s.upper()
            turn += 1
            
        i += 1
    
    return answer
```

정말 막풀었다.. ㄷ 그런데도 통과되지 못하고 풀지못하였다. n진법 쪽에 많이 약해서 그런듯하다.. 진법문제를 많이 풀어봐야겠다.

### 다른사람의 풀이를 참고 풀이

```python
big = ["A", "B", "C", "D", "E", "F"]

def solution(n, t, m, p):
    a = "0"
    i = 0
    
    while True:
        if len(a) >= t*m:
                break
        
        b = ""
        j = i
        
        while j:
            if (j % n) > 9:
                b = big[(j % n) - 10] + b
            else:
                b = str(j % n) + b
            
            j = j // n              

        a += b
        i += 1
    
    answer = a[p-1::m][:t]
    
    return answer
```

이 풀이는 내 접근방식과는 다르게 해당 진법의 숫자문자열을 만든 뒤, 해당 숫자문자열을 차례에 맞게 슬라이싱 하여 풀이한 문제이다.

아직 진법 문제가 생소하여 비슷한 문제를 많이 풀어봐야겠다!