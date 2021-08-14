# 문제 - https://www.acmicpc.net/problem/3273

import sys

input = sys.stdin.readline

# 입력
N = int(input())
nums = list(map(int, input().split()))
target = int(input())

# nums 정렬
nums.sort()

# target이 되는 쌍의 횟수
cnt = 0
# 왼쪽, 오른쪽 포인터
l, r = 0, len(nums) - 1

# 왼쪽 포인터와 오른쪽포인터가 만나면 종료
while l < r:
    # 정렬된 값의 양 투포인터 쌍의 합의 타겟보다 작으면 왼쪽 포인터 증가
    if nums[l] + nums[r] < target:
        l += 1
    # 정렬된 값의 양 투포인터 쌍의 합의 타겟보다 크면 오른쪽 포인터 감소
    elif nums[l] + nums[r] > target:
        r -= 1
    # 투포인터 쌍의 합이 타겟과 같으면 투 포인터 모두 안쪽으로 이동 및 카운트
    else:
        cnt += 1
        l += 1
        r -= 1

print(cnt)
