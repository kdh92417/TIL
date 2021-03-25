n = int(input())

# 원판이 옮기는 과정을 담는 리스트 생성
result = []

# Move Function
def move_peg(start, end):
    result.append(f"{start} {end}")


def hanoi(num, start, end):
    # Except
    if num == 0:
        return 0

    # Base Case
    if num == 1:
        return move_peg(start, end)

    # Recursive Case
    else:
        other_peg = 6 - (start + end)

        hanoi(num - 1, start=start, end=other_peg)
        move_peg(start=start, end=end)
        hanoi(num - 1, start=other_peg, end=end)
    return

# 입력받은 n의 값을 인풋으로 hanoi 함수 실행
hanoi(n, 1, 3)

# 원판이 최소로 움직이는 횟수와 과정을 출력
print(len(result))
for i in result:
    print(i)
