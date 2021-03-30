# 내가 푼 풀이
def solution(n):
    answer = 0

    result = []

    for i in range(1, n + 1):

        for j in range(1, n+1):

            if i * j == n:
                result.append(i)

    answer = sum(result) 
    return answer


# 다른 사람의 더낫은 풀이
'''
def solution(n):
    answer = 0

    # n을 매 루프의 인덱스로 나눈값이 0 이면 약수
    # 약수들의 합을 합쳐서 반환
    return answer + sum([i for i in range(1, n + 1) if n % i == 0])
'''