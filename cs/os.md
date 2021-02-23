# 1. 운영체제

## 1. 1 운영체제란?

- OS (Operating System)
- 사용자가 컴퓨터를 쉽게 다루게 해주는 인터페이스
- 컴퓨터 자원을 효율적으로 관리하기 위한 시스템
- 공통된 소프트웨어 플랫폼
- 컴퓨터 응용 프로그램 관리자
- 시스템 하드웨어를 관리할 뿐 아니라 응용 소프트웨어를 실행하기 위하여 하드웨어 추상화 플랫폼과 공통 시스템 서비스를 제공하는 시스템 소프트웨어

**즉, 응용 프로그램과 하드웨어의 중간 다리이자 관리자이다.**

<br>

## 1. 2 운영체제의 구조 이해

### 리눅스

- 운영체제의 한종류
- 그래픽보다는 안정성에 초점을 둔 OS
- 콘솔환경으로 적합한 OS
- 오픈소스
- Architecture

  ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/48126e4e-1ca7-48b3-8cbe-cb4eff2f69f4/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/48126e4e-1ca7-48b3-8cbe-cb4eff2f69f4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210223T073207Z&X-Amz-Expires=86400&X-Amz-Signature=328cc92e2868cd02a71b98f47f61441bbde887f83b46600c8181df9791a06566&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### 유닉스

- 리눅스의 부모
- 리눅스와 유사
- 유닉스의 일부분을 떼와 IOS를 만듬

<br>

# 2. 운영체제 구성 요소

OS의 구성요소로 미들웨어와 펌웨어가 있다.

## 2. 1 어디까지가 운영체제?

### 미들웨어

- 운영체제에서 제공하는 서비스 이외에 추가적으로 이용 가능한 서비스를 제공하는 컴퓨터웨어
- 사용자 쪽의 가까운 운영체제

### 펌웨어

- 전자기기 등의 기본적인 제어 및 구동을 담당하는 '하드웨어를 위한 소프트웨어'
- 변경이 필요 없는 특화된 운영체제
- 차량용 OS, 공유기, CCTV, 리모컨등
- 하드웨어쪽에 가까운 운영체제

<br>

## 2. 2 운영체제 구성요소

**사실 운영체제는 커널(Kernel)이 핵심(심장)**

- 보안, 자원 관리(프로세스, 메모리), 하드웨어 추상화
- 블루 스크린 = 커널 패닉 = 운영체제가 멈췄다.

  ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/48c2b83a-273a-4a07-8122-7eca7b5e699a/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/48c2b83a-273a-4a07-8122-7eca7b5e699a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210223T073249Z&X-Amz-Expires=86400&X-Amz-Signature=b440b373b001d3859349a9e8fb964f6d0753829485a13227c0236cdb7570beb5&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

**쉘**

- 사용자의 지시를 해석해 커널에게 전달
- 윈도우 탐색기, 리눅스 터미널

**시스템 콜(System Call)**

- 사용자 영역에서 커널 영역에 작업을 요청하는 방법

<br>

# 3. 운영체제 핵심 기능

## 3. 1 프로세스 - OS

- **프로그램 vs 프로세스**

  - 프로그램 : 특정 작업을 수행하는 일련의 명령어들의 모음
  - 프로세스 : 사용자의 명령을 OS가 받아 메모리에 올리는 순간부터(실행) 종료되는 시점
    - 실행중인 프로그램

- **프로세스 vs 서비스**
  - 둘다 특정 기능을 수행하는 프로그램을 의미, but
  - 목적이 다르다
  - **프로세스 : 사용자와 상호 작용하는 프로그램 (코어)**
  - **서비스 : 백그라운드에서 실행되는 정기 작업을 담당(데몬)**
    - 서비스도 프로세스와 마찬가지로 실행중인 프로그램이다.
    - 하지만 서비스는 상호작용하지 않고 계속 정기적인 작업 알아서 하는 백그라운프로그램.
  - 웹 서비스 개발 == 프로그램 개발 ?

<br>

## 3. 2 프로세스 - DEV

---

**프로세스 vs 스레드**

- 프로세스 : 하나의 프로그램 단위(독립 공간을 가짐) - 아파트 한층
- 스레드 : 하나의 실행 흐름 단위 (공간 공유) - 고시원

<br>

## 3. 3 병렬(Parellel)

### 병렬 프로그래밍

- 동시에 여러 작업을 해야할 때 사용하는 기술
- **멀티 프로세스** : 특정 작업을 여러 프로세스에서 동시 처리
  - 부모와 자식 프로세스 관계를 가진다.
  - 문맥 교환이 필요 + 부하가 크지만 안정성 괜찮다.
- **멀티 스레드 :** 여러 작업을 여러 스레드를 동시 처리
  - 데드락 : 주요 자원에 배타적인 읽기 / 쓰기 작업 미보장 시 발생
  - 동기화 : 공유 자원 동기화
  - 매우 어렵다.

### 데드락(교착 상태)

- 이도 저도 아무것도 안되는 상황
- 대안 : 뮤텍스, 이벤트 , 세마포어, 타이머

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/da9fe0a1-b523-48c4-b7d4-edb438889c49/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/da9fe0a1-b523-48c4-b7d4-edb438889c49/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210223T073347Z&X-Amz-Expires=86400&X-Amz-Signature=48872e82485f9235b7a323544829b5b044d05f0686a2ec00f4bc688b9a85d814&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

<br>

## 3. 4 동기화(Synchronization)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/370caf0b-eb2a-4a88-80de-454d10a3701b/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/370caf0b-eb2a-4a88-80de-454d10a3701b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210223T073406Z&X-Amz-Expires=86400&X-Amz-Signature=0c6c8504dd25e20c23ec95fdd2b0c594c9dd49829b496da36c46c93b94b4b540&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### **멀티 스레드의 한계**

- 새로운 사용자 = 새로운 스레드 = 부하 증가
- 멀티 스레드는 결국 순차적인 처리를 빠르게 하는 것
- 엄청나게 많은 사용자는 서버 다운의 원인이 됨
- 자원 공유는 항상 어려움

### **동기(Sync)와 비동기(Async)**

- 동기 처리 : 순차적으로 일을 처리하는 방식(lock-free)
- 비동기 처리 : 일당백. 이거 하면서 저것도 하자
- 동기와 비동기는 동시에 여러 작업을 수행한다는 점은 같다.
- 하지만 자원을 동기 와 비동기는 자원을 엇떻게 뿌려주는 방식이 다르다
  - 동기 : 열쇠키가 하나
  - 비동기 : 지문등록(위임)

<br>

## 3. 5 메모리 관리

### 운영체제의 메모리 관리

- **분할** : 페이징(고정 크기)과 세그먼테이션(유동 크기)
- **보호** : 다른 프로세스 메모리 영역에 접근하지 못하도록 강제
- 가상 메모리
  - 메모리의 효율적 관리 : '지금' 필요한 코드만 메모리에 올려서 쓰자
  - 메모리 관리의 단순화 : 프로세스마다 통일된 주소 공간 배치
  - 메모리 용량 및 안정성 보장 : 프로세스들 간의 메모리 침범 최소화

<br>

### OS - 스케줄링

OS가 하는 역활

- **디스크에서 메모리로**

  - 디스크에 있는 데이터를 메모리의어디로, 어떻게 올릴래?
  - 최적 / 최초 / 순환 / 최악 적합

- **메모리에서 CPU로**
  - CPU는 한 번에 하나의 명령어만 처리할 수 있다.
  - 동시에 여러 개의 프로세스를 실행할 수 있는 이유? = 스케줄링
  - 기다렸다가 들어가는 비선점형 / 강제로 뺏는 선점형

<br>

### 메모리관리 - DEV

**개발자와 메모리**

- 코드는 이미 정해져 있으며, 메모리에 탑재 후 실행
- 임시로 데이터를 저장할 공간이 필요하다 :: 메모리
  - 스택 : 바로바로 썼다가 지웠다가 할 수 있는 공간
  - 힙 : 특정 크기의 공간이 필요한 경우 (할당 - 해제)

**할당과 해제**

- 임시 저장 공간은 무조건 메모리 공간을 필요로 한다.
- 할당 했다면 반드시 해제할 것
- 알아서 해 주는 언어는 고민하지 않아도 될까?

**메모리 생명 주기**

- 언어에 상관없이 `할당 - 사용 - 해제` 주기를 가진다.
- 할당(allocate) : 명시적으로 OS에 요청하거나 대신 해주거나
- 사용(use) : 변수에 값을 쓰고 읽는 실질적인 작업을 수행
- 해제(release) : 사용이 끝난 메모리는 다시 OS에게 반환

**메모리 누수(Memory Leak)**

- 프로그램에서 필요로 하지 않는 메모리를 계속 점유하는 현상
- 단순 손실로 끝나지 않음. 속도 저하! 해킹 공격!
- 검색! 자바스크립트는 어떻게 작동하는가: 메모리관리

**메모리 오염(Memory Corruption)**

- 개발자가 의도하지 않은 메모리 덮어쓰기 또는 접근
- 메모리 누수가 원인이 되기도 한다.
- 잘못된 코드 사용이 대부분의 원인이 됨 ⇒ BSOD!

<br>

## 3. 6 파일 시스템, 드라이버

### 파일 시스템

- 물리적인 디스크의 파티션 내에서 데이터를 배치하고 관리하기 위한 체계
- 모든 파일은 헤더와 데이터를 가진다.
- 모든 파일은 header에 meta 정보가 들어가 있고 data에 그파일의 내용이 담겨져 있다.

### 디바이스 드라이버

응용프로그램이 하드웨어를 직접 다루고 싶을때 쓰인다 (e.g 화상채팅앱이 노트북의 캠을 직접 사용하고 싶을때)

**시스템 라이브 러리**

- 운영체제 내부에 정의된 기능을 응용프로그램에서 사용할 수 있도록 제공하는 함수 집합

**디바이스 드라이버**

- 운영체제와 장치들 사이의 상호 통신을 허용하는 소프트웨어 구성요소 또는 코드(.sys)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cb1589ae-4793-4ac0-bb8e-390852515af8/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cb1589ae-4793-4ac0-bb8e-390852515af8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210223T073538Z&X-Amz-Expires=86400&X-Amz-Signature=0bf3d105805bd0342dc4ed32abe7a4d94600aa39b0c3413416216693c56c43e1&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)