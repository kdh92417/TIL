# Programmers - N으로 표현

- [문제](https://programmers.co.kr/learn/courses/30/lessons/42895)

<br>

## 풀이

해당 문제는 다른 사람의 풀이를 여러차례보고 구글링 검색하여 코드를 베껴서 봐도 도저히 이해도 안되었다 ㅜㅜ.. 그래서 몇시간 계속 이해하던 끝에 중요한 점은

- 해당 횟수로 조합이 될 수 있는 경우의 수이다.
    ```
    N을 n번 사용해서 만들 수 있는 수 :
    N을 n번 연달아서 사용할 수 있는 수들의 집합
    N을 1번 사용했을 때 SET 과 n-1번 사용했을 때 SET을 사칙연산한 수들의 집합
    N을 2번 사용했을 때 SET 과 n-2번 사용했을 때 SET을 사칙연산한 수들의 집합
    ...
    N을 n-1번 사용했을 때 SET 과 1번 사용했을 때 SET을 사칙연산한 수들의 집합
    ```

위의 원리를 이용하여 내가 참고한 블로그에서는 밑의 풀이와 같이 풀이를 하였다.

```python
def solution(N, number):
    # 예외 처리
    if N == number:
        return 1
    
    # 8회 횟수까지 set 자료형으로 초기화
    # set() * 8 : 이렇게해서 set 자료형을 초기화하면 모든 인덱스의 set자료형이 같은 id를 바라보기 떄문에 쓰면 안된다.
    dp = [set() for i in range(8)]
    
    # ('N' * i) 을 각 횟수마다 추가
    for idx, _set in enumerate(dp):
        _set.add(int(str(N) * (idx + 1)))

    # 각 횟수마다 반복
    for i in range(1, 8):
        # 조합이 될 수 있는 횟수만큼 반복
        # 5 => (1, 4), (2, 3), (3, 2), (4, 1)
        # 3 => (1, 2), (2, 1)
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i - j - 1]:
                    # 사칙연산의 경우의 수 추가
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0: dp[i].add(op1 // op2)
        
        # 해당 횟수에서 number가 있을경우 i + 1 리턴
        if number in dp[i]:
            return i + 1
    # 없을 경우 -1
    else:
        return -1
```

<br>

## 참고

- [프로그래머스-코딩 테스트 고득점 kit N으로 표현](https://gurumee92.tistory.com/164)