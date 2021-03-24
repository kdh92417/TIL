# 합병 정렬

<br>

## Divide and Conquer 방식으로 합병 정렬하기

### 단계

1. Divide : 리스트를 반으로 나눈다.

2. Conquer : 왼쪽 리스트와 오른쪽 리스트를 각각 정렬한다.

3. Combine : 정렬된 두 리스트를 하나의 정렬된 리스트로 합병한다.

<br>

## 정렬된 리스트 2개를 합병정렬 시키기

```python
def merge(list1, list2):
    # 정렬된 항목들을 담을 리스트
    merged_list = []

    # list1이나 list2의 요소가 없을 경우 예외 처리
    if not list1 or not list2:
        return list1 + list2

    # 반복문을 돌면서 각 리스트에서 0번째 인덱스를 뽑아서 정렬된 리스트에 추가
    while list1 and list2:
        if list1[0] > list2[0]:
            merged_list.append(list2.pop(0))
        else:
            merged_list.append(list1.pop(0))

    # 정렬된 리스트와 남은 리스트를 합쳐서 반환
    return merged_list + list1 + list2

# 테스트
print(merge([1], []))
print(merge([], [1]))
print(merge([2], [1]))
print(merge([1, 2, 3, 4], [5, 6, 7, 8]))
print(merge([5, 6, 7, 8], [1, 2, 3, 4]))
print(merge([4, 7, 8, 9], [1, 3, 6, 10]))
```
