# Fraudulent Activity Notifications

## 타임초과된 나의 풀이

```python
def activityNotifications(expenditure, d):
    i = 0
    count = 0

    while i+d < len(expenditure):
        sort_list = sorted(expenditure[i:i+d])
        mid = len(sort_list) // 2
        
        if d % 2 == 0:
            median = (sort_list[mid] + sort_list[mid - 1]) / 2
        else:
            median = sort_list[mid]
            
        if expenditure[i+d] >= median * 2:
            count +=1

        i += 1
    return count
```

- 아무래도 `sorted()` 내장함수에 리스트슬라이싱을 동시에 써서 시간복잡도가 많이 안 좋아진 것 같다. 이것을 좀 고쳐봐야겠다.

