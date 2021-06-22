# Number Line Jumps

- https://www.hackerrank.com/challenges/kangaroo/problem

## 문제

캥거루 1과 캥거루 2가 각각 다른 위치에서 다른 점프간격으로 앞으로 나아간다. 이때 캥거루1과 캥거루2가 만나는지 만나지 않는지 확인하는 문제이다.

## 풀이

```python
def kangaroo(x1, v1, x2, v2):
    # 항상 x1 < x2 이니 v1보다 v2가 같거나 크다면 두 캥거루는 만날 수 없다.
    if v1 <= v2:
        return 'NO'

    # 두 캥거루의 위치 설정
    c1, c2 = x1, x2
    # 점프 횟수
    i = 1

    # 캥거루1의 거리가 캥거루2의 거리보다 작거나 같을때 반복
    while c1 <= c2:
        # 두캥거루가 만나면 YES
        if c1 == c2:
            return 'YES'
        c1 += i*v1
        c2 += i*v2
    
    # 캥거루1과 캥거루2가 만나지 못함
    return 'NO' 
```

- 두캥거루의 시작지점과 점프횟수를 비교하여 캥거루1이 캥거루2보다 아직 앞서나가지못할때까지 반복문을 돌려서 캥거루1과 캥거루2가 만나는지 확인하였다.