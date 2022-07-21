# 소프트웨어 아키텍처

## 소프트웨어 아키텍처란?

> 소프트웨어 개발관점에서 아키텍처는 소프트웨어의 전체적인 구조를 잡아주는 설계도

- 아키텍처는 세세한 코드를 보지 않더라도 일관된 코드구조로 흐름을 유추할 수 있도록 한다.
- 모듈과 객체설계에 대한 고민의 방향을 제시해준다.

<br>

## 아키텍처가 없다면?

- 본인이 작성한 코드나 모듈을 프로젝트 어느곳에 두어야될지 모른다.
  -> 고민과 결정의 시간이 든다.
- 본인이 생각한 기준이 팀원과 다를 수 있다. -> 네이밍이 일관성이 없게된다.
- 폴더, 파일간의 관계가 복잡해진다. -> 컴포넌트를 나누기 힘들어진다.
- 새로운 사람이 프로젝트를 보게되면 어디서 어떻게 봐야될지 감이 오지 않는다. -> 전체적인 흐름과 설계를 이해하는데 시간이 오래걸린다.

- __특히 개발 지속되어질수록 산발적으로 코드가 작성되고 기존코드를 이해하기 어려워져 개발의 생산성이 떨어진다.__

<br>

### 설계-체력 가설(Design Stamina Hypothesis) - Martin Fowler

> 아키텍처가 없는 개발은 초반에는 빠른 생산성을 가지지만, 개발이 지속되어질수록 생산성이 떨이지고,
> 좋은 아키텍처가 있는 개발은 초반에 생산성이 떨어지지만 개발이 지속되어질수록 점차 생산성이 증가한다.

![마틴 파울러](https://user-images.githubusercontent.com/58774316/172128024-208fd485-e654-45d6-b9b1-563d995145bf.png)


<br>

## 아키텍처가 있다면?

### 1. 시스템에 규칙을 만든다.

- 코드가 일관적 -> 견고한 코드가 됨
- 모듈과 추상화에대한 고민을 덜어줌 -> 코드 생산성 증대

### 2. 소프트웨어의 구성을 한눈에 파악

- 아키텍처를 파악하면 전체적인 시스템에대한 흐름을 유추 -> 코드를 파악하거나 작성하는 시간이 적게듬
- 개발자들간의 커뮤니케이션 비용 절감

### 3. 좋은 아키텍처 -> 테스트를 쉽게 만든다.

- 좋은 테스트코드는 코드의 변동에도 동작에 문제가 없도록 보장한다.
- 좋은 아키텍처 & 테스트 & 소프트웨어의 지속 개발

<br>

## 트레이드오프(등가교환)

> 좋은 아키텍처를 선택하고 도입이 항상 좋은 것은 아니다. (비용 발생)

- 초반에 아키텍처를 고민하고 결정하는 시간 필요
- 코드를 작성하거나 읽을때 알아야될 규칙이 증가
- 팀원 전체가 프로젝트의 아키텍처 패턴에 익숙해야됨
- 전반적으로 코드의 양이 증가

> 문제상황과 앞으로의 프로젝트 방향성이 정해지지 않았다면, 기본적인 작업흐름을 유지하면서 개발을 하고
> 나중에 본격적으로 아키텍처 도입을 고려해보는 것도 하나의 방법

<br>


## TIP

### 1. 의존성 관계에 집중하는 것이 아키텍처를 쉽게 이해하는 지름길

- 아키텍처의 핵심은 곧 컴포넌트별로 역할을 명확하게 나누고 의존관계에 있다.

### 2. 아키텍처 패턴을 적용한 다른사람들의 코드를 참고

- 다른사람들이 아키텍처패턴을 적용한 코드나 시스템을 참고하여 나 자신만의 코드로 작성해야 나의 것이 됨
