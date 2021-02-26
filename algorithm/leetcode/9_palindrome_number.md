# 9. Palindrome Number

## 문제

파라미터로 정수 x가 주어지는데, 이때 이 정수 x가 팰린드롬 정수인지 판별하는 문제이다.
(거꾸로 숫자를 읽어도 똑같은 것)

<br>

## My Solution

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 예외처리 부분
        if x < 0:
            return False
        if x < 10:
            return True

        # temp에 거꾸로 된 숫자를 만들어 비교
        result = 0
        i = 10
        temp = x
        while x != 0:
            result *= 10
            result += (x % 10)
            x = x // 10

        return temp == result
```
