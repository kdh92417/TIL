# 종류별 테스트

## 1. 유닛 테스트

> 함수나 메서드 같이 작은 단위의 코드에서 입출력의 결과가 올바른지 확인하는 테스트

### Code Example

```python
def create_token(user_id: str) -> str:
    return user_id + "_verified"

def test_create_token():
    actual = create_token("adam")
    expected = "adam_verified"
    assert actual == expected
```

<br>

## 2. 통합 테스트 (Integration Test)

> 여러 요소를 통합한 테스트 <br>
>  &nbsp;  → 여러 함수와 클래스가 엮인 로직이 잘 작동하는지 확인

<br>

### Code Example

- Login Function
  ```python
  def login(user_id: str, user_password: str) -> str:
      user_repository = UserRepository()  # DAO
      user = user_repository.find_by_id(user_id)
      if user.id == user_id and user.password == user_password:
          return create_token(user_id)
      else:
          raise Exception("Login authentication failed")
  ```
  - `Login` 함수는 `create_token()`와 `UserRepository()`에 의존

<br>

- 통합 테스트 코드 작성
  ```python
  def test_login_successful():
      # given
      user_id = 'adam'
      user_pw = '1234'

      # when
      actual = login(user_id, user_pw)
    
      # then
      assert actual == 'adam_verified'

  def test_login_failed():
      # given
      user_id = "adam"
      user_password = "wrong pw"

      # when & then
      with pytest.raises(Exception):
          login(user_id, user_password)
  ```
  - 의존하는 함수 `create_token()`와 객체 `UserRepository()`를 모두 테스트
  
### 요약

- 통합테스트는 의존성 있는 객체들의 정상 작동 여부까지 포함하는 테스트
- 통합테스트는 외부 의존성을 포함하고 있는 경우가 많다 → 테스트 환경은 운영환경과 분리(예를 들어서 운영 DB와 연동되어져 있으면 안된다.)
- 테스트에서 재현할 수 없는 외부 의존성(운영 데이터베이스, 운영 API 서버등)은 테스트 더블을 사용

<br>

## 3. E2E 테스트 (Feat. Docker Compose)

> 최종 사용자 입장에서의 테스트


- 유닛테스트와 통합테스트에 타겟이 되는 코드들도 같이 테스트되긴하지만 너무 포곽적
    
    → 유닛테스트와, 통합테스트를  따로 테스팅
