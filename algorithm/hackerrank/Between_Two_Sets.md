# Between Two Sets

- https://www.hackerrank.com/challenges/between-two-sets/problem

## 문제

두개의 배열 a, b가 주어지는데 `a` 배열의 공배수와 `b` 배열의 공약수중 같은 숫자가 몇개인지 알아내는 문제이다.

## 풀이

```python
def getTotalX(a, b):

    # a배열과 b배열의 공약수와 공배수가 같은 수는 a배열과 b배열 사이에 있기 때문에 검사할 경계값 설정
    max_num = max(a)
    min_num = min(b)

    # 공배수 리스트
    cm = []
    # 공배수와 공약수가 같은 수 카운트
    result = 0

    # a의 공배수
    for i in range(max_num, min_num+1, max_num):
        count = 0
        for j in a:
            if i % j == 0:
                count += 1
        if count == len(a):
            cm.append(i)

    # a의 공배수중 b의 공약수가 있는지 검사
    for i in cm:
        count = 0
        for j in b:
            if j % i == 0:
                count += 1
        if count == len(b):
            result += 1
    return result
```

- 문제를 해석하는 것 부터가 어려운 문제였다. 결국은 a배열의 공배수와 b배열의 공약수중 같은수가 몇개인지 확인하는 문제이다.

나는 a배열의 공배수를 먼저 찾아내고 a배열의 공배수 중에서 b배열의 공약수가 있는지 확인하여 풀이하였다.

하지만 중첩반복문을 써서 시간복잡도가 O(n<sup>2</sup>)이다. 시간복잡도를 더 줄여야겠다.



```python
# highest common factor(리스트의 최대 공배수)
def get_hcf(arr):
    hcf = arr[0]
    for i in arr:
        hcf = gcd(hcf, i)
    return hcf

# least common multiple(최대 공약수)
# 유클리제호제법
def lcm(a, b):
    return int(a*b / gcd(a,b))

# 리스트의 최소공배수
def get_lcm(arr):
    l = arr[0]
    for i in arr:
        l = lcm(l, i)
    return l

def getTotalX(a, b):
    # a배열의 최소공배수
    lcm_a = get_lcm(a)
    # b배열의 최대공약수
    hcf_b = get_hcf(b)

    # lcm_a <= 검색할 범위 <=lcm_b
    count = sum([1 for i in range(lcm_a, hcf_b + 1, lcm_a) if i % lcm_a == 0 and hcf_b % i == 0])
    return count
```

### 풀이 순서
1. `a` 배열의 최소공배수(`lcm_a`)와 `b`배열의 최대공약수(`hcf_b`)를 구하여 그 범위내에서 카운트한다.
2. `lcm_a` 배수의 값으로 곱하면 a배열의 공배수가 되고 `hcf_b`값으로 나눈값이 0라는 소리는 b배열의 공약수로 나눈다는 뜻이다.
3. 조건에 맞는 수를 카운트하여 리턴(여기서는 `sum()`을 활용)

> 최소공배수와 최대공약수를 활용하여 범위를 줄이고 시간복잡도도 O(n Log n)으로 위의 풀이보다 나아졌다.


