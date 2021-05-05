## 왜 자료구조를 공부해야될까?

```python
import time

test_list = [x for x in range(0, 1000001)]
test_set = set([x for x in range(0, 1000001)])

t_0 = time.time()
print(1000000 in test_list)
t_1 = time.time()

print("리스트에서 걸린 시간 : {}".format(t_1 - t_0))

t_0 = time.time()
print(100000 in test_set)
t_1 = time.time()

print("set 에서 걸린 시간 : {}".format(t_1 - t_0))

# True
# 리스트에서 걸린 시간 : 0.019809961318969727
# True
# set 에서 걸린 시간 : 7.152557373046875e-06
```

위의 예시에서 보이듯 100000숫자를 찾는데 List자료형보다 Set자료형이 약 3000배정도 빠른 것이 보인다. 이처럼 어떤 자료구조를 어떤 상황에 쓰느냐에 따라서 성능이 달라진다.
