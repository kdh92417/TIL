# Greedy Algorithm

미래를 내다보지 않고, 당장 눈 앞에 보이는 최적의 선택을 하는 방식

- 장점 : 간단하고 빠르다
- 단점 : 최적의 답이 보장되지 않는다.

## 최적 부분 구조 (Optima Substructure)

부분 문제들의 최적의 답을 이용해서 기존 문제의 최적의 답을 구할 수 있음

## 탐용적 선택 속성 (Greedy Choice Property)

각 단계에서의 탐욕스런 선택이 최종 답을 구하기 위한 최적의

<br>

### 문제

최소 동전으로 돈을 거슬러 주는 함수를 Greedy Algorithm으로 구현

- 이문제 안에는 최적 부분구조와 탐욕적 선택속성이 있어서 Greedy Algorithm으로 풀면 최적의 솔루션을 구할 수 있다.

- 풀이

```python
def min_coin_count(value, coin_list):
    # 누적 동전 갯수
    count = 0

    # 탐욕적으로 보기위해 동전이 큰순서부터 본다
    for coin in sorted(coin_list, reverse=True):
        count += (value // coin)
        value %= coin

    return count
```

- 처음에 난 if문을 걸어서 (value // coin) > 0 경우만 봤엇는데 사실 어차피 count에 더하는 것도 value에 나머지 연산하는 것도 걸필요가 없었다.

<br>

### 문제

현재 프린트물을 출력해야하는데, 지각인 상태이다. 각각 사람당 출력해야할 페이지수를 파라미터로 받아서 최소의 시간으로 모두 페이지를 출력할 수 있도록 하는 것이다.

```python
def min_fee(pages_to_print):
    # 인풋으로 받은 리스트를 정렬시켜 준다
    sorted_list = sorted(pages_to_print)

    # 총 벌금을 담을 변수
    result = 0

    # 정렬된 리스트에서 총 벌금 계산
    for page in range(len(sorted_list)):
        result += sorted_list[page] * (len(sorted_list) - page)

    return result


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
```

- 최소의 프린트물을 출력해야하는 학생이 먼저 출력해야 전체 출력시간이 짧아지기 때문에 탐욕속성을 갖고있다.
- [6, 11, 4, 1]의 출력할 페이지수를 가진 리스트를 받을 때

```
첫번째 사람이 지각하는 시간 = 1
두번째 사람이 지각하는 시간 = 1 + 4
세번째 사람이 지각하는 시간 = 1 + 4 + 6
네번째 사람이 지각하는 시간 = 1 + 4 + 6 + 11
```

- 이므로 최적부분구조를 가지고있다.
- 따라서 Greedy Algorithm 으로 풀면 최적의 솔루션으로 풀 수 있다.
