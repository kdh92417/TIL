# 백준 2675

import sys

# 라인 전체 입력받음
input = sys.stdin.readline

T = int(input())
result = ''

# 한줄 입력받을 때마다 문자열의 한 요소마다 반복 횟수 r을 곱하여 result에 더함
for i in range(T):
    line = input().split()
    r, s = int(line[0]), line[-1]
    result = ''
    for j in s:
        result += (j*r)
    print(result)
    
    
"""

인터넷으로 찾아보니 입력받을 때

r, s = input().split()으로 받으면 공백기준으로 따로 입력받을 수 있엇음

"""