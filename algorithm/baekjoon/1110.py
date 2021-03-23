# 백준 1110번

import sys
input = sys.stdin.readline

n = int(input())

origin = n
count = 0

while True:
    if (n < 0) or (n > 99):
        print(0)
        
        break

    first_num = n // 10
    second_num = n % 10
    merge_num = (first_num + second_num) % 10

    count += 1
    n = (second_num * 10) + merge_num

    if n == origin:
        print(count)
        break