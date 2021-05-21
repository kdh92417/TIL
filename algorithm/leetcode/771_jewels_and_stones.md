# 문제

- [Hash 문제 - Leet Code 771](https://leetcode.com/problems/jewels-and-stones/)

- 인풋으로 보석과 돌이 주어지는데 돌의 각요소에서 보석의 요소가 몇개나 있는지 검사하는 문제이다.

## 분석

이 문제는 갖고 있는 돌 S의 각각의 개수를 모두 헤아린 다음, J의 각 요소를 키로하는 각 개수를 합산하면 풀이할 수 있다. 

> 따라서 해시 테이블로 풀이할 수 있는 전형적인 문제이다.

## 나의 풀이
```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Counter 함수로 보석의 요소를 키로 만듬
        jew = Counter(jewels)
        
        # 돌의 요소중 보석이 있는 지 검사
        cnt = 0
        for s in stones:
            if s in jew:
                cnt += 1
                
        return cnt
```

- input `jewels`을 딕트로 만들어 돌의 요소중 보석이 있는지 검사하여 풀었다.

- 반복문안에서 매번 보석의 요소를 들어다 보기 때문에 시간복잡도는 O(n<sup>2</sup>) 인것 같다.



## Counter을 이용한 계산 생략

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # 돌의 빈도수 계산 및 딕트화
        s = Counter(stones)
        
        # 보석의 요소를 키값으로 빈도수 계산
        cnt = 0
        for char in jewels:
            cnt += s[char]
                
        return cnt
```

- 위의 풀이와는 반대로 돌을 Counter로 요소를 키값으로 돌 요소의 빈도수를 밸류값으로 만들었다.

- 그리고 Counter는 없는 키값은 에러처리가 되는것이 아니라 0으로 처리가 되서 위와같은 풀이가 가능하다.

- 결국 보석요소를 키값으로 결과값에 더해주면된다.

> 해시로 테이블로 만들어 반복문 한번만 돌고 그안에서 O(1)의 탐색을 하기 때문에 `O(n)` 이다.


## 파이써닉한 풀이

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)
```

- `sum()` 과 ListComprehension을 이용하여 한줄로 코드를 줄였다.