# 테스트 코드 작성

## 개념

테스트의 종류는 크게 3개
- 유닛 테스트 : 가장 작은 단위의 테스트
- 통합 테스트 : 통합적인 로직을 테스트
- E2E(End to End) 테스트 : 클라이언트 입장에서 테스트

테스트 작성은 보통 `유닛 테스트` -> `통합테스트` -> `E2E` 순으로 작성

<br>

## 테스트코드


1. `pytest` 설치
```shell
pip install pytest
```

2. test code 작성
```python
def add(a, b):
    return a + b

# test_ : 테스트하고싶은 함수 앞에 test_를 prefix해줘야됨
def test_add():
    a, b = 1, 2
    assert add(a, b) == 3
```

3. 테스트 실행
```python
# terminal에서
python -m pytest test_example.py
```



## Tip

- PyCharm : `preferences` -> `pytest` 검색 -> `Testing` 항목을 `pytest`로 바꾸면 함수별로 테스트 가능
