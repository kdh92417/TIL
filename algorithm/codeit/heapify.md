# Heapify 함수 구현하기

- 힙 속성이 아닌 트리를 부모노드가 자식노드보다 크게 정렬

## 내가 구현한 Heapify함수

```python
def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp


def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    # 자식노드가 없으면 트리 리턴
    if left_child_index > tree_size:
        return tree

    # 부모와 자식노드중 최대값 찾기
    max_num = max(tree[index], tree[left_child_index], tree[right_child_index])

    # 왼쪽 노드가 클 경우
    if max_num == tree[left_child_index]:
        swap(tree, index, left_child_index)
        return heapify(tree, left_child_index, tree_size)

    # 오른쪽 노드가 클 경
    elif max_num == tree[right_child_index]:
        swap(tree, index, right_child_index)
        return heapify(tree, right_child_index, tree_size)

    return tree



# 실행 코드
tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
print(tree)
```

## Codeit 풀이

```python
def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp

def heapify(tree, index, tree_size):
    """heapify 함수"""

    # 왼쪽 자식 노드의 인덱스와 오른쪽 자식 노드의 인덱스를 계산
    left_child_index = 2 * index
    right_child_index = 2 * index + 1

    largest = index  # 일단 부모 노드의 값이 가장 크다고 설정

    # 왼쪽 자식 노드의 값과 비교
    if 0 < left_child_index < tree_size and tree[largest] < tree[left_child_index]:
        largest = left_child_index

    # 오른쪽 자식 노드의 값과 비교
    if 0 < right_child_index < tree_size and tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index: # 부모 노드의 값이 자식 노드의 값보다 작으면
        swap(tree, index, largest)  # 부모 노드와 최댓값을 가진 자식 노드의 위치를 바꿔준다
        heapify(tree, largest, tree_size)  # 자리가 바뀌어 자식 노드가 된 기존의 부모 노드를대상으로 또 heapify 함수를 호출한다
```

- 이 풀이가 조금 더 깔끔하고 간결한 것 같다.