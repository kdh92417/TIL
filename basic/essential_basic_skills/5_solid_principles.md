# 객체 지향의 5대 원칙 SOLID

## SRP (Single Responsibility Principle)

- 하나의 객체는 하나의 책임만을 지녀야한다는 원칙


## OCP(Open Closed Principle - 개방 폐쇄 원칙)

- 확장에는 열려있고, 수정에는 닫혀있게 해야한다는 법칙
- 보통 추상 클래스를 통해 추상화 시키고, 이를 상속 구현하게 하여 원칙을 지키게 한다.

## LSP(Liskov Substitution Principle - 리스코브 치환 원칙)

- 부모 객체의 역할은 자식 객체도 할 수 있어야 된다는 원칙
- 상속보다는 구성 ( 무조건 상속이 좋은 것은 아니다. )