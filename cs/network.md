## 목차

1. [네트워크란?](#1-네트워크란?)
2. [프로토콜 (Protocol)](<#2-프로토콜-(protocol)>)
3. [네트워크와 인터넷](#3-네트워크와-인터넷)
4. [주소체계](#4-주소체계)
5. [전송, 응용계층](#5-전송,-응용계층)
6. [브라우저 통신](#6-브라우저-통신)

# 1. 네트워크란?

- 노드들이 서로 자원을 공유할 수 있도록 허용하는 통신망
- 네트워크 기능이 없는 컴퓨터는 이제 깡통이나 다름 없음
- 프로그램에도 네트워크 기능 구현이 필요하게 되었음

<br>

## 1. 1 이것이 네트워크

### 소규모 네트워크 예시

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1dc6c55f-4359-4b47-80ef-2311a72592de/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1dc6c55f-4359-4b47-80ef-2311a72592de/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082210Z&X-Amz-Expires=86400&X-Amz-Signature=112313152a56b9c177c6bc6f9ac67733e95ab3027e8e2fcef8e06b322646ea53&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### 회사 네트워크 예시

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/62622a72-40ca-4b98-8abe-45c3582e8c33/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/62622a72-40ca-4b98-8abe-45c3582e8c33/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082234Z&X-Amz-Expires=86400&X-Amz-Signature=5552d345e381c3b7bb00e1eff36388ee3b0c77b11463a92a96431e2815047faf&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### 대륙간 네트워크

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/458095cb-4977-4570-86cd-5ce36e283ef5/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/458095cb-4977-4570-86cd-5ce36e283ef5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082250Z&X-Amz-Expires=86400&X-Amz-Signature=89d29ace27fc8b81afa56a7a308e7f981430ff0a6187e3856d5bbd8d669d13fc&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

<br>
<br>

# 2. 프로토콜 (Protocol)

- 네트워크 상의 위치한 컴퓨터들간의 공동규칙 또는 약속
- 네트워크 사이에서 메세지를 주고 받는 양식과 규칙 체계
- 프로토콜 == 네트워크 구조?

<br>

## 2. 1 네트워크 프로토콜 : OSI 7 계층, TCP / IP 모델

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c37bde48-b572-44c1-9aca-51c302fb53eb/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c37bde48-b572-44c1-9aca-51c302fb53eb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082335Z&X-Amz-Expires=86400&X-Amz-Signature=a560bfd9d767c1cb2ae08c91c699e6f3b870fa852adf9eee16cc0fe1c77bcdbe&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/863864c0-8df2-4ec9-b936-11f5938be9e2/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/863864c0-8df2-4ec9-b936-11f5938be9e2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082351Z&X-Amz-Expires=86400&X-Amz-Signature=67d0678e0ff18d851709e133a5c9d85608d197a032eeadf6090ec4c524a413c1&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### OSI 7 계층 - 이상적인 구조

- OSI 7 계층 : user app에서 OS를 거쳐 Hardware까지의 길에서 만나는 계층들
- 국제표준화기구(ISO)에서 개발한 모델
- 컴퓨터 네트워크 프로토콜 디자인과 통신을 계층으로 나눈 것

### TCP / IP 모델 - 현실적인 구조

- ISO 7 Layer는 현실과는 거리가 좀 있음
- 실질적인 통신에 필요한 규약을 정의할 필요가 있음

| OSI 7                        | TCP / IP    | Explain                   |
| ---------------------------- | ----------- | ------------------------- |
| Application (응용 계층)      | Application | 실질적인 서비스 제공      |
| Presentation (표현 계층)     | Application | 압축, 암/복호화 - 번역    |
| Session (세션 계층)          | Application | 통신 관리 방법 계층       |
| Transport (전송 계층)        | Transport   | 신뢰성 있는 데이터 전달   |
| Network (네트워크 계층)      | Internet    | 여러 네트워크를 거친 전달 |
| Data-Link (데이터 링크 계층) | Link        | Point-to-Point 통신       |
| Physical (물리 계층)         | Link        | 물리적인 연결             |

[OSI 7 & TCP / IP](https://www.notion.so/b871fdef70974d3a9dbfb736aaa9432c)

### How use it?

- 네트워크 기능을 탑재한 모든 프로그램(OS 포함)은 이 프로토콜에 맞춰 통신을 해야 한다.
- **캡슐화** : 보내고 싶은 데이터가 있다면 차례대로 캡슐을 씌워 전송해야된다.
- 데이터를 받는 쪽에서도 캡슐을 하나씩 차례대로 해제한 후 그 안에 담긴 메세지를 확인 가능
- 개발자는 아래쪽에 위치한 계층을 몰라도 됨: OS 역활

### 캡슐화

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6fd11f45-daf3-4ea7-bdff-db47f16f37b8/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/6fd11f45-daf3-4ea7-bdff-db47f16f37b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082608Z&X-Amz-Expires=86400&X-Amz-Signature=bc3256c882b9a4960283547fc12a10cf2cdc586fd6e44c2ee3fb2ed51b7f15ca&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

- 캡슐를 입힌다 : 정보를 답는다.
- 캡슐을 벗긴다 : 정보를 빼서 해석한다.

<br>

## 2. 2 채팅과 프로토콜

### 예시

- 메신저앱에서 메시지를 전송하는 상황

  ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4fa10c74-ee72-4b85-8570-6b0dbb9b1387/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4fa10c74-ee72-4b85-8570-6b0dbb9b1387/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082628Z&X-Amz-Expires=86400&X-Amz-Signature=1734a23ac9df0a2cf2d89f78f8debb4b7ec41be788c14bd12f4159d6df985913&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

<br>
<br>

# 3. 네트워크와 인터넷

<br>

## 3. 1 근거리 네트워크

### Point-to-Point 연결

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/91ade4cf-cf87-4002-a342-706a4a6d7fe9/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/91ade4cf-cf87-4002-a342-706a4a6d7fe9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082714Z&X-Amz-Expires=86400&X-Amz-Signature=6d0b164c34c63b95453dc1dcaf40ae9b3f9b1aa4cd11875fa721aa5d15ef8cf2&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

**PPP(Point-to-Point Protocol) - 점대점 통신 약속(두대의 PC)**

- 두 통신 노드 간의 직접적인 연결을 위해 사용
- Data-Link Protocol
- 사실 둘만 대화 잘 되면 복잡한 프로토콜 필요 없음

<br>

### Local Area Network

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dca91ec3-c738-4769-9bda-a2f117236dfd/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/dca91ec3-c738-4769-9bda-a2f117236dfd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082732Z&X-Amz-Expires=86400&X-Amz-Signature=28e8bb69f0c2784616840d235fb0168a9e88b49ead919ef93e04c65e8a8c6bfd&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

<br>

### **근거리 통신망. LAN의 등장(1964)**

- 한정된 지역에서 컴퓨터를 기본으로 하는 여러 전자기기 사이의 자유로운 정보교환
- 여기서부터 네트워크라는 용어가 의미를 가진다.
- 여럿이 통신하려면 주소가 필요
  - MAC(Media Access Control):NIC 주소
  - **00:0C:29:09:93:6A 몇비트 일까?**
- 서로 내가 먼저 통신하려고 싸우면?
  - CSMA / CD : 잘 보고 들어가고, 충돌나면 그 사실을 컴퓨터가 알 수 있도록 해 주는 기술

<br>

## 3. 2 이것이 인터넷

### **LAN 토폴로지 : 통신망 구조**

- 이 컴퓨터들을 어떤 모양으로 연결해야될까?
- LAN 토폴로지 : 통신망 구조

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/887691f2-4544-4c3b-a985-0ffca92e0861/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/887691f2-4544-4c3b-a985-0ffca92e0861/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082845Z&X-Amz-Expires=86400&X-Amz-Signature=a74a3371ecbc67b452295bba51045ca479c446b69a32b119153865f649bcec45&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

- 웹서버는 Star Topology 방식을 따른다.

### 연결 장치

- 더미 허브(Hub) : 그냥 연결만 해줄 뿐
- 스위치 : 데이터 전달만 하는 것이 아니라 데이터흐름 나름 제어하는 장치 (안정적임)

### 광역 통신망. WAN

- 광역 통신망 (네트워크를 확장)
- 서로 다른 네트워크를 연결
- MAC 주소로 통신을?
  - 대규모 네트워크를 고려해서 만든 주소가 아님.
  - 다른 대체 수단이 필요함! **Internet Protocal(IP)**

### 인터넷

- 인터넷 프로토콜 스위트(TCP/IP)를 기반으로 하여 전세계적으로 연결된 컴퓨터 네트워크
- Deep Web ?

<br>
<br>

# 4. 주소체계

## 4. 1 인터넷 프로토콜 (IP)

- 인터넷을 하기 위한 프로토콜
- IP주소 : 인터넷 상에서 컴퓨터를 찾아가기 위해 사용하는 주소
- 정의, 역활, 헤더(spec)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fd163f31-4d07-4da7-9a03-c14f1ecd75b8/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fd163f31-4d07-4da7-9a03-c14f1ecd75b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082905Z&X-Amz-Expires=86400&X-Amz-Signature=497299d893e7c10dadc105a932da09f2de6af7bf8a56bd88160af200d316cfe4&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c37bde48-b572-44c1-9aca-51c302fb53eb/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/c37bde48-b572-44c1-9aca-51c302fb53eb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082335Z&X-Amz-Expires=86400&X-Amz-Signature=a560bfd9d767c1cb2ae08c91c699e6f3b870fa852adf9eee16cc0fe1c77bcdbe&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

### 생각해 볼 문제

- 213.42.102.34 / 192.168.0.1 / 1.1.1.1 / 127.0.0.1 ——> $8bit$ ($2^8 = 256$) $* 4 = 32 bit$
- 최대로 할당 가능한 IP 개수?
- IP 주소 / Netmask / Gateway / DNS
- 공인 IP / 사설 IP
  - 실제 사용하는 IP / 한 IP로 공유하는 별칭 IP
- 유동 IP vs 고정 IP
  - IP 주소가 제한적이기때문에 일일이 IP주소를 부여해줄 수 없다.
- IP 대역이 어떻게 되나요?
- 서버 주소가 어떻게 돼?
- 지금의 IP로는 부족하다! (IPv4 → IPv6)
- ipconfig / ifconfig : 사설대역
- whatismyip : 공인 IP

<br>
<br>

## 4. 2 라우팅

- 다른 네트워크는 어떻게 찾아갈까?
- 목적지 네트워크 까지 최단시간에 가기위해

### 라우터

- 네트워크 길잡이(=L3 스위치)
- 목적지를 찾아가기 위한 경로 정보를 제공
- 라우팅 프로토콜: OSPF, IGRP, RIP BGP 등
- 지금 맞닿아있는 경로정보를 가지고 있다.
- 라우팅 경로 명령어 : `traceroute` `주소`

<br>
<br>

# 5. 전송, 응용계층

## 5. 1 연결 방식 - TCP

- IP가 엇떻게 통신하지? 라는 것이었다면, TCP는 연결해서 엇떻게 대화를 주고받지? 이다.

### TCP(Transmission Control Protocol) - 전화

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5517ea54-4618-483f-a0b2-9dc17f362113/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5517ea54-4618-483f-a0b2-9dc17f362113/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082933Z&X-Amz-Expires=86400&X-Amz-Signature=eef781a06add9e9b5265677d7175ba36be28e44824f6ebe6a5d16a1a16cb5cd1&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

- 전송 제어 프로토콜 : 신뢰성 있는 연결 성립을 위한 프로토콜
- 신뢰성 보장, 혼잡 제어, 흐름 제어 (netstat - an)
- 실전화 같은 느낌
- 각각의 프로그램은 포트에 연결되어있고 실제로 연결되는 것은 포트와 포트끼리

### 3-Way Handshaking

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e819f85b-bfb6-4a12-b73b-7df2576f35a5/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/e819f85b-bfb6-4a12-b73b-7df2576f35a5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T082946Z&X-Amz-Expires=86400&X-Amz-Signature=c7cb9220181e8d4279ff86b76e16033ae6a400817fe02e15d0abdf0cff3ef23a&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

- 전송 제어 프로토콜 : 신뢰성 있는 연결 성립을 위한 프로토콜
- 서로간에 통신을 하겠다고 선언을 한 후 대화를 하자(암구어)
- 대화가 종료된 다음에는? 근데 귀찮게 매번 이렇게 해야돼?

<br>

## 5. 2 UDT(User Datagram Protocol) - 우편

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/170246ec-bb6f-4b53-b018-27a804fd9328/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/170246ec-bb6f-4b53-b018-27a804fd9328/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T083001Z&X-Amz-Expires=86400&X-Amz-Signature=8420baff926d04cbbb8bf1b47aa48722c200d32fc6c8c898ac41fc2fc2623ca1&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

- 편지가 간혹 안 갈때도 있지만 그런 일은 거의 없다.
- 모든 연결을 신뢰성있게 해야 하는 것은 아니다!
  - FPS 게임에서 총 쏠 때!
  - 영상 스트리밍할 때!
- 3-Way Handshaking 없이 그냥 툭 던진다.

<br>

## 5. 3 Port : 네트워크 통신의 종단점

- 포트가 열려있다! - 외부와의 연결 채널이 열렸다.
- 통신을 한다 - 해당 포트의 규격(프로토콜)으로 서로가 대화한다.
- 포트번호 1~65535번 (1~1023번은 well-known 포트)
- 실습: netstat
- 이용할때는 포트를 신경쓰지 않아도 되지만, 제공해야될때는 포트를 신경써야된다.
- **80포트, 443포트는 웹개발할 때 쓰이니 기억하기바람**

### Well-known 포트

- 자주 쓰는, 반드시 필요한 포트는 번호를 정해놓고 쓴다.
- 만약, 포트 번호를 지키지 않는다면?

### 새로운 프로그램을 개발했다. 어떤 포트를 쓸까?

- 포트를 쓴다는 것은 무슨 의미일까?
- 개발자가 어디까지 신경써야 할까?

<br>
<br>

# 6 브라우저 통신

## 6. 1 브라우저에서 [www.google.com](http://www.google.com) 을 접속한다?

- www.google.com은 주소인가? - 도메인!
- 사람은 숫자보다 단어에 강하다
- 도메인 주소는 실제 통신에 사용되는 주소가 아니다!

<br>

## 6. 2 DNS(Domain Name System) - 프로토콜

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4dae3e13-cf83-4e45-b6f6-06799b5096a6/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/4dae3e13-cf83-4e45-b6f6-06799b5096a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T083017Z&X-Amz-Expires=86400&X-Amz-Signature=d7715d867019d3878f2275014bf6c20bbb86dbf6489ed435b555f09dd8a4cf99&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

- 도메인 네임 시스템
- 도메인 이름을 네트워크 주소로 바꾸거나 그 반대를 수행

### DNS 서버

**Server**

- 클라이언트에게 네트워크를 통해 정보나 서비스를 제공하는 컴퓨터(server computer) 또는 프로그램(server program)
- 클라이언트(Client) = 서버에 접속 가능한 프로그램이나 서비스
- DNS 서버 : 도메인 이름을 해석해 주는 서버(실습:nslookup)

**두 컴퓨터가 통신을 하려면**

- 양쪽 다 채널이 열려 있어야하고(포트)
- 통신을 기다리는 쪽(서버)과 시작하는 쪽(클라이언트)이 필요하고
- 통신하는 방식에 대한 합의가 필요(프로토콜)

<br>

## 6. 3 HTTP

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/59bb0644-93dc-4413-83e2-113f10eb10a7/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/59bb0644-93dc-4413-83e2-113f10eb10a7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T083150Z&X-Amz-Expires=86400&X-Amz-Signature=fef6dfbf0f95b9255783d26b988a44ab0ad9b803ec913393522b9d3d2a582118&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

- Application 계층에서 존재한다. (DNS도 마찬가지)
- HyperText Transfer Protocol
- www 상에서 정보를 주고받을 수 있는 프로토콜
- 우리가 보통 `웹통신`이라고 부르는 것을 가능하게 해 줌

### WWW(World Wide Web)

- 인터넷에 연결된 컴퓨터를 통해 정보를 공유할 수 있는 정보 공간
- HTTP로 연결하고, 데이터는 HTML로 공유한다.

### Stateless 프로토콜

- 각각의 요청을 독립적인 트랜잭션으로 취급하는 프로토콜
- HTTP : 사용자끼리는 몰라도 된다.

### Stateful 프로토콜

- 서버 내부 상태 유지를 요구하는 프로토콜
- TCP : 세션을 맺고 지속적으로 유지한다.

### HTTP 헤더

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f3d87282-e5d1-4a7b-8367-e81b612510ef/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/f3d87282-e5d1-4a7b-8367-e81b612510ef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T083223Z&X-Amz-Expires=86400&X-Amz-Signature=5d998e107fe323078e7ea1cab7f728f6d5d2909939573d93d53d10bbbe3936a0&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

<br>

## 6. 4 와이 파이

- 컴퓨터 시스템들이 무선랜에 연결할 수 있도록 해주는 기술
- 무선랜(Wireless LAN)

  - IEEE 802.11 표준을 기반으로 하는 무선 통신 기술
  - Wifi 와 OSI 7 Layer

  ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/120806f1-2742-417f-a502-666f30b1968f/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/120806f1-2742-417f-a502-666f30b1968f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210224T083244Z&X-Amz-Expires=86400&X-Amz-Signature=7798167e2511caf35bf24bef35fcaefd3125a09ad01f03376963c0f2a5d2b3e9&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)
