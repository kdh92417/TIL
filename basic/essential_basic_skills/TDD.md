# TDD(Test Driven Development) 기본 개념

> 테스트가 개발을 이끌어가는 방법론 

- 테스트코드를 먼저 작성함으로써 
  -> 개발사항과 각 기능의 입/출력 요구사항을 코드로 문서화한 후 기능을 개발

<br>

## TDD Example

> 간단한 쇼핑몰 웹사이트의 백엔드 서버에서 로그인 기능을 개발해야되는 상황


- 요구사항
  1. `POST /login` 으로 `user_id`와 `user_password`를 json을 실어 요청하면 -> `token`을 응답 받아야된다.

  2. `token` 은 `user_id`에 `_verified`가 붙은 문자열

<br>

### 1. 테스트 작성

```python
def test_login_endpoint():
    # given
    api_host = "http://localhost:8000"
    payload = {
        "id": "adam",
        "password": "1234"
    }

    # when
    res = requests.post(url=f"{api_host}/login", json=payload)

    # then
    assert res.data() == {
        "token": "adam_verified"
    }
```

- 결과 : 실패
  - 서버실행 x
  - 해당 엔드포인트에 `POST method`로 날린 `request`를 처리하는 로직이 없다.

<br>

### 2. 테스트 대상 구현

```python
@app.post("/login")
def login_endpoint(req: LoginRequest):
    user_id = req.id
    user_password = req.password

    user_repository = UserRepository()  # DB와 연동되어 User 정보를 저장하고 불러오는 객체
    user = user_repository.find_by_id(user_id)
    if user_id == user.id and user.password == user_password:
        token = user_id + "_verified"
    else:
        raise Exception("로그인 인증에 실패했습니다.")

    return {
        "token": token
    }
```

<br>

### 3. 테스트 대상 리팩토링

- SRP (Single Responsibility Principle) 지키기

  - http 요청과 응답을 주고 받는 책임을 담당하는 함수
  - 로그인 로직을 실행을 담당하는 함수
  - 토큰 생성 로직을 담당하는 함수

<br>

1. 테스트코드 작성
    ```python
    def test_login_successful():
        # given
        user_id = "grab"
        user_password = "1234"
        
        # when
        actual = login(user_id, user_password)
        
        # then
        assert actual == "grab_verified"
        
        
    def test_login_failed():
        # given
        user_id = "grab"
        user_password = "wrong password"
        
        # when & then
        with pytest.raises(Exception):
            login(user_id, user_password)
    ```

2. `login()` 함수의 입/출력을 정의
    ```python
    def login(user_id: str, user_password: str) -> str:
        user_repository = UserRepository()  # DB와 연동되어 User 정보를 저장하고 불러오는 객체
        user = user_repository.find_by_id(user_id)
        if user_id == user.id and user.password == user_password:
            # 토큰 생성 로직은 create_token() 함수에 위임합니다.
            return create_token(user_id)
        else:
            raise Exception("로그인 인증에 실패했습니다.")
    ```

3. `create_token()` 함수의 테스트코드 작성
    ```python
    def test_create_token():
        actual = create_token("grab")
        expected = "grab_verified"
        assert actual == expected
    ```

4. `create_token()` 함수 구현
    ```python
    def create_token(user_id: str) -> str:
        return user_id + "_verified"
    ```

5. `login_endpoint()` 함수 리팩토링
    ```python
    from fastapi import FastAPI
    from dataclasses import dataclass

    app = FastAPI()

    @dataclass
    class LoginRequest:
        id: str
        password: str
            
            
    @app.post("/login")
    def login_endpoint(req: LoginRequest):
        # 로그인 로직은 login() 함수에 위임합니다.
        token = login(user_id=req.id, user_password=req.password)
        return {
            "token": token
        }
    ```

### TIP

> 위의 TDD는 `Top-Down` 방식으로 작성하였지만 `Bottom-Up` 방식으로도 작성 할 수 있다.

<br>

## 레드-그린-리팩토링

> 위의 TDD가 레드-그린-리팩토링

<br>

![](https://user-images.githubusercontent.com/58774316/170513452-7ab81725-6804-4d89-a2d5-6e25b6b0d9f4.png)

### 과정

1. 테스트 작성 (RED)
   - 테스트할 대상이 구현 X -> 테스트 실패

2. 테스트가 통과되도록 작성 (GREEN)
    - 구현이 완료 -> 테스트 성공

3. 기존 코드를 필요에 따라 리팩토링 (BLUE)
    - 기존 동작에 영향을 주면 안된다. 즉, 입/출력은 변하지 않고 내부동작만 바꿔야됨
    - 리팩토링은 종종 사이드이펙트를 불러오기도 함
    - 하지만 테스트 코드로 사이드이펙트 체크 가능
    - 리팩토링 실패 -> 테스트 실패, 리팩토링 성공 -> 테스트 성공

<br>

## TDD의 장점

### 장점

- 테스트 코드를 먼저 작성하면 -> 입/출력과 발생하는 예외를 무엇으로 정의 해야할지 명확하다.

- 꼼꼼하게 테스트 작성

- 테스트 코드가 깔끔한 코드 사용 문서가 됨 (이해가 잘 안됨)

### 단점
- 테스트가 가능하도록 코드를 설계하는 것이 어렵다.
  - TDD를 진행하게 되면 모든 코드들이 테스트가 가능하도록 설계해야됨
  - 테스트가 가능하도록 코드를 설계하려면 추상화, 의존성 주입등을 잘 활용해야됨
  - 테스트 환경 구축(Docker Compose, DB 데이터 초기화)의 작업이 번거롭다.

- TDD가 익숙하지 않으면 개발프로세스가 느려질 수 있다.

> 상황에 맞게 유동적으로 TDD를 적용해야된다.