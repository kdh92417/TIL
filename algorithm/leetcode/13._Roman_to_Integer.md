# 13. Roman to Integer

Roman numerals를 파라미터로 입력받아 integer로 변환하는 문제이다.

## 풀이

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # 로마 숫자를 dict에 저장
        rom_num = {
            'I' : 1,
            'X' : 10,
            'C' : 100,
            'M' : 1000,
            'V' : 5,
            'L' : 50,
            'D' : 500
        }

        # 0부터 마지막인덱스 - 1까지 반복하면서 다음인덱스의 값이
        # 현재인덱스의 값보다 * 5 or * 10 일때를 따로 계산하고
        # result에 더하고, 인덱스 += 2
        i, result = 0, 0
        while i < len(s) - 1:
            if rom_num[s[i + 1]] == rom_num[s[i]] * 5 or rom_num[s[i + 1]] == rom_num[s[i]] * 10:
                result += rom_num[s[i + 1]] - rom_num[s[i]]
                i += 2
            else:
                result += rom_num[s[i]]
                i += 1

        if i < len(s):
            result += rom_num[s[-1]]

        return result
```

<br>

이렇게 풀었는데 애초에 이렇게 풀지말고, 다른사람들이 풀이를 보니 인덱스를 거꾸로 돌면서 인덱스 다음 값이 현재 인덱스보다 크면 더해주고 아니면 빼주면 되는 걸로 쉽게 풀 수 있엇다.

더 낫은 풀이법

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        rom_num = {
            'I' : 1,
            'X' : 10,
            'C' : 100,
            'M' : 1000,
            'V' : 5,
            'L' : 50,
            'D' : 500
        }

        # 인덱스 이전값과 결과값 변수 설정
        prev, res = 0, 0
        for i in s[::-1]:
            # 현재 인덱스가 그전인덱스보다 크다면 res += rom_num[i] 아니면 빼기
            if rom_num[i] >= prev:
                res += rom_num[i]
            else:
                res -= rom_num[i]
            # 매루프마다 prev 변수에 그전 인덱스의 값 설정
            prev = rom_num[i]

        return res
```
