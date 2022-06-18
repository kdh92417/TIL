# 모놀리스 와 마이크로서비스 아키텍처


![모놀리스 아키텍처와 마이크로서비스 아키텍처](https://user-images.githubusercontent.com/58774316/174092805-e988a073-efb4-401d-9b1f-e96f489adb60.png)

<br>

## 모놀리스 아키텍처

> 모놀리스 아키텍처는 하나의 소프트웨어를 구성하는 모든 모듈과 코드를 한 프로젝트에서 관리하는 것
> 
> 단일 프로젝트 실행이 곧 애플리케이션 실행


![image](https://user-images.githubusercontent.com/58774316/174093188-70c9dc00-0880-400f-a2a3-5946f2e77d21.png)
(출처: https://www.n-ix.com/microservices-vs-monolith-which-architecture-best-choice-your-business/)

<br>

### Monolithic Structure Example

```
app/
  domain/
    users/
      model.py
      repository.py
    products/
      model.py
      repository.py
    payment/
      model.py
      repository.py
  service/
    user_service.py
    product_service.py
    payment_service.py
  controller/
    user_controller.py
    product_controller.py
    payment_controller.py
  main.py
  config.json

```

- `app` 내에 모든 모듈이 존재
- 하나의 프로젝트안에 모든 것이 담김
- main.py 실행 -> 애플리케이션 실행

<br>

### 모놀리스의 장단점

__장점__
- 한 프로젝트내에 모든 모듈과 코드가 존재하여 개발과 리뷰에 용이
- 소프트웨어 구조가 단순하여 애플리케이션의 전체적인 흐름과 구성을 이해하기 쉽다.
- `main.py` 만 실행하면 애플리케이션이 실행되기 때문에 배포가 쉽다.
- 디버깅이나 장애대응이 쉽다.

__단점__
- 개발이 진행될 수록 코드가 많아지고 서비스가 확장되면 코드흐름을 이해하기 쉽지 않다.
- 한프로젝트 내에서 모든 코드가 결합되어 코드변경과 확장이 힘들다.
- 테스트와 빌드의 양이 점점 많아져 테스트속도 및 빌드속도가 매우 느려짐
- 하나에 코드가 모든 코드에 영향이 가기때문에 -> 최신 기술 스택 도입의 어려움


<br>
<br>

## 마이크로서비스 아키텍처

> 마이크로서비스 아키텍처는 하나의 소프트웨어를 구성하는 컴포넌트를 독립적인 프로젝트들로 분리하여 관리하는 것을 말한다.

> 각 컴포넌트를 마이크로 서비스라 부를 수 있다.

> 개발과 배포를 각 마이크로서비스별로 진행

> 하나의 애플리케이션이 정상 작동하기 위해서는 각각의 마이크로서비스가 모두 정상 작동해야됨

> 소프트웨어가 점점 복잡해지고 커질때 마이크로서비스가 필요

<br>

![image](https://user-images.githubusercontent.com/58774316/174096560-b187e689-2d4b-474e-ba1a-7e0b35eaf01c.png)
(출처: https://www.n-ix.com/microservices-vs-monolith-which-architecture-best-choice-your-business/)

<br>

### Microservice Structure Example

- `User Domain`
  ```
  app/
    domain/
      model.py
    service/
      user_service.py
    controller/
      user_controller.py
    main.py
    config.json
  ```

- `Product Domain`
  ```
  app/
    domain/
      model.py
    service/
      product_service.py
    controller/
      product_controller.py
    main.py
    config.json
  ```

- `Payment Domain`
  ```
  app/
    domain/
      model.py
    service/
      payment_service.py
    controller/
      payment_controller.py
    main.py
    config.json
  ```

<br>

### 마이크로서비스의 장단점

__장점__
- 컴포넌트 별로 독립적인 프로젝트를 구성
  - 각 컴포넌트 별로 코드의 구조와 흐름을 이해하기 쉽다.
  - 각 마이크로서비스마다 결합도가 강하지 않다. -> 확장가 수정에 용이
  - 개발이 진행되어질 수록 생산성 향상
  - 테스트와 빌드, 배포의 속도가 향상
  - 컴퓨팅 리소스를 다르게 줄 수 있다. -> 서버 확장에 용이
  - 기술 스택을 다양하게 가질 수 있다. (User -> Python, Product -> Java, Payment -> Go)

__단점__
- 여러 서비스를 통합하여 테스트할 때 난이도 상승
- 마이크로서비스의 각 컴포넌트별로 기준을 정하는 것이 어렵다.
- 독립적인 마이크로서비스를 개발하다보면 전체 애플리케이션의 큰 그림을 파악하기 어려울때도 있음
- 여러 서비스에 걸친 분산 시스템 환경에서 고민할 문제들이 많다.
