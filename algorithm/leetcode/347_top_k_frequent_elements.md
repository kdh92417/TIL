# 347. Top K Frequent Elements

비어있지 않은 정수 배열이 주어졌을 때, 가장 많이 등장하는 k개의 원소를 반환하라.

## Counter와 sorted함수를 이용한 풀이

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = [i[0] for i in sorted(Counter(nums).items(), key=(lambda x:x[1]), reverse=True)]
        return answer[:k]
```

- heap을 이용하지 않고 Counter와 sorted함수를 이용하여 풀었다.

## heap모듈을 이용한 풀이

```python
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), count.get)
```

- heapq 모듈의 `nlargest` 함수를 이용한 k개의 빈번한 수를 반환한 풀이이다.



