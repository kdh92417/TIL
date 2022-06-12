# 핵사고날 아키텍처 (Hexagonal Architecture)

> 애플리케이션을 중심으로 보고 다른 외적인 것들(ex. DB, Framework)을 교체할 수 있는 부품으로 보는 아키텍처 들이 주목받기 시작함. 대표적인 아키텍처로 `헥사고날 아키텍처` 와 `클린 아키텍처` 가 있다.
>
> 이중 헥사고날 아키텍처는 애플리케이션을 중심으로 보고 그외의 모듈들은 애플리케이션에서 제공하는 포트 모양만 맞다면 언제든 바꿀 수 있다고보는 아키텍처
>
> 어댑터가 포트모양만 맞으면 동작하는 것을 보고 `포트 앤 어댑터(Ports-and-Adapters)라고도 부른다.`

<img src="https://user-images.githubusercontent.com/58774316/173237035-37363722-e78b-4785-aa17-14280b391120.png" style="display: block; margin:30px auto; width:80%;" art="출처 : https://livebook.manning.com/book/microservices-patterns/chapter-2/53">

(출처 : https://livebook.manning.com/book/microservices-patterns/chapter-2/53)


<br>

## 구조

### 1 도메인
- 레이어드 아키텍처에서의 도메인 레이어와 개념이 같다.
- 애플리케이션의 핵심이 되는 도메인

### 2. 애플리케이션
- 도메인을 이용한 애플리케이션 로직을 제공
- 관용적으로 `Service` 라고 불림
- 포트는 어댑터를 끼울 수 있는 인터페이스(추상클래스)
- `Inbound Port` : 애플리케이션으로 흐름이 들어오는 포트
- `Outbound Port` : 애플리케이션에서 흐름이 나가는 포트

### 3. 어댑터
- 애플리케이션 내에서 포트에 끼울 수 있는 구현체(추상클래스 상속받아서 인터페이스 구현)
- `web` 또는 `cli` 등은 인바운드 포트에 끼울 수 있는 인바운드 포트를 이용
- `db`등은 아웃바운드 포트에 끼울 수 있는 아웃바운드 포트를 이용

<br>

## 의존성 흐름

> 어댑터 -> 애플리케이션 -> 도메인

- 위의 역행하는 의존성흐름이 되면 안된다. (ex. 비즈니스 로직 -> 어댑터, 도메인 -> 어댑터)

<br>

## Example

### 헥사고날 아키텍처 프로젝트 구조 예시

```
src/
  adapter/              ### 어댑터 레이어
    inbound/
      api/
        product_controller.py
        user_controller.py
        ...
    outbound/
      repositories/
        product_repository.py
  	    user_repository.py
  application/         ### 애플리케이션 레이어
    service/
      product_service.py
      user_service.py
    port/
      inbound/
        product_port.py
        user_port.py
      outbound/
        product_repository.py
        user_repository.py
  domain/              ### 도메인 레이어
    product.py
    user.py

```

- __as-is__ : 레이어드 아키텍처에서는 서비스 레이어(비즈니스 로직) 에서 인프라스트럭쳐에(DB) 있는 모듈을 사용
  ```python
  # src/application_layer/product_service.py

  from src.domain_layer import product
  from src.infrastructure_layer.database import db
  from src.infrastructure_layer.repositories import product_repository

  def create_product(name: str, price: str) -> bool:
      ...
      product_repository = product_repository.ProductRepository(session)
      ...
  ```

- __to-be__ : 포트를 이용하여 DB 모듈 사용
  ```python
  # src/application/service/product_service.py

  from src.domain import product
  from src.applicaiton.port.outbound.product_repository import ProductRepository  # 이 부분이 수정되었습니다!
  # 이제 애플리케이션 레이어는 인프라스트럭쳐 레이어가 아닌 애플리케이션 레이어에 의존합니다

  def create_product(name: str, price: str, product_repository: ProductRepository) -> bool:
      ...
      product_repository.create(...)
      ...
  ```

> 포트 앤 어댑터의 의존성 원칙은 저수준이 아닌 고수준에 의존 (의존성 역전 원칙이라 볼 수 있음)
>
> 보통 컴파일 의존성에서는 고수준을 의존 한 후, 런타임에서 의존성을 주입(의존성 주입 프레임워크를 많이 활용)

###  