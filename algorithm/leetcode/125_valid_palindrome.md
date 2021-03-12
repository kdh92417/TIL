# 125. Valid Palindrome

주어진 문자 s 를 팰린드롬 여부, 즉 앞뒤가 바뀌어도 똑같은지 확인하는 문제이다.

## for 문을 이용한 풀이

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        for i in range(len(strs)):
            if strs[i] != strs[-(i +1)]:
                return False

        return True
```

- 반복문을 이용하여 각 첫항과 마지막항을 비교하여 같은지 비교

## 정규표현식을 이용한 풀이

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # re 모듈의 sub메소드를 통해 소문자 스트링 s의 공백을 제거
        s = re.sub('[^a-z0-9]', '', s.lower())

        # 리스트 슬라이싱을 이용하여 비교
        return s == s[::-1]
```

- 정규식 표현을 이용하면 별다른 알고리즘을 이용할 필요없이 간단하게 해결할 수 있다.
