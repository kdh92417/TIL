# HTTP 프로토콜 완벽 정리

## HTTP 프로토콜 이란?

웹 서버와 웹 클라이언트 사이에서 데이터를 주고받기 위해 사용하는 통신 방식으로, TCP/IP 프로토콜 위에서 동작합니다. 즉, 우리가 웹을 이용하려면 웹서버와 웹 클라이언트는 각각 TCP/IP 동작에 필수적인 IP 주소를 가져야 한다는 의미이다.

- HTTP는 HTML이나 XML 과 같은 하이퍼 텍스트 뿐만 아니라 이미지, 음성, 동영상, 자바스크립트, PDF와 각종 도큐먼트 파일 등 컴퓨터에서 다룰 수 있는 데이터라면 무엇이든 전송할 수 있다.
- 예를 들어, 주소창에 `[www.google.com](http://www.google.com)` 을 입력하고 `Enter` 를 누르면 웹 클라이언트와 웹 서버 사이에 HTTP 연결이 맺어지고, 웹 클라이언트는 웹 서버에 HTTP 요청 메시지를 보내게 된다. 웹 서버는 요청에 따른 처리를 진행한 후 그 결과를 웹 클라이언트에게 HTTP 응답 메시지로 보냅니다. 이런 방식으로 요청 메시지와 응답 메시지가 반복적으로 오가면서 웹을 사용하게 되는 것이다.

<br>

![http](https://user-images.githubusercontent.com/58774316/111725057-ab511380-88a9-11eb-80da-68cc9bf45d5f.png)

<br>

## HTTP 메세지의 구조

HTTP 메시지는 클라이언트에서 서버로 보내는 요청 메시지와 서버에서 클라이언트로 보내는 응답 메시지 2가지가 있다.

![message](https://user-images.githubusercontent.com/58774316/111723207-87d89980-88a6-11eb-9c1b-36f28e3b41a8.png)

<br>

**시작줄 / 헤더 / 바디** 로 나눌 수 있다.

- **시작줄**
  - Request 시, 메서드와 요청 URL, HTTP version ( GET /exam/help.txt HTTP/1.1 )
  - Response 시, HTTP version, 상태 코드 및 사유 구절 ( HTTP/1.1 200 OK )
- **헤더**
  - 요청과 응답 메세지에 대한 추가적인 정보를 담고 있다.
  - Key/Value 형식으로 나타냄
- **바디**

  - 전송하고 싶은 실질적인 데이터를 나타냄
  - 헤더를 마치고 \n(CRLF : 공백) 후에 나타남.

<br>
<br>

- 요청 메세지 예제

```cpp
GET /hello.txt HTTP/1.1 		// 요청메서드 / 자원주소 / HTTP 버전
User-Agent: curl/7.16.3 libcurl/7.16.3 OpenSSL/0.9.7l zlib/1.2.3	// 헤더
Host: www.example.com												// 헤더
Accept-Language: en, mi
```

- 응답 메세지 예제

```cpp
HTTP/1.1 200 OK         // HTTP 버전 / 응답코드 및 사유
Date: Mon, 27 Jul 2009 12:28:53 GMT    // 바디까지 주욱 헤더
Server: Apache
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
ETag: "34aa387-d-1568eb00"
Accept-Ranges: bytes
Content-Length: 51
Vary: Accept-Encoding
Content-Type: text/plain

Hello World! My payload includes a trailing CRLF.	// 바디
```

<br>

## HTTP 처리 방식

위에서 살펴본 URL을 이용하여 우리는 서버에게 자원을 요청 할 수 있는데요, 이 때(요청할때) 데이터에게 특정 동작을 수행하고 싶을 때 HTTP Request Methods를 이용합니다.

일반적으로 HTTP 요청 메소드는 HTTP Verbs라고도 불리우며 아래와 같이 주요 메서드를 갖고 있습니다.

<br>

| Method Name |               의미               | CRUD와 매핑되는 역활 |
| :---------: | :------------------------------: | :------------------: |
|     GET     |    존재하는 자원에 대한 요청     |         READ         |
|    POST     |        새로운 자원을 생성        |        Create        |
|     PUT     |    존재하는 자원에 대한 변경     |        Update        |
|   DELETE    |    존재하는 자원에 대한 삭제     |        Delete        |
|    HEAD     |  리소스의 헤더(메타데이터) 취득  |                      |
|   OPTIONS   | 서버 옵션들을 확인하기 위한 요청 |                      |
|    TRACE    |        루프백 시험에 사용        |                      |
|   CONNECT   | 프록시 동작의 터널 접속으로 변경 |                      |

<br>

위의 정의한 바와 같이 데이터에 대한 조회, 생성, 변경, 삭제 동작을 HTTP 요청 메소드로 이용할 수 있습니다. 참고로 때에 따라서는 POST 메서드로 PUT, DELETE의 동작도 수행할 수 있습니다.

<br>

## HTTP Status Code

위에서 살펴본 HTTP 요청 메서드가 클라이언트에서 설정하는 정보라면 HTTP 상태 코드는 클라이언트에서 요청을 받아 응답(Response)을 해주기 위해 설정해주는 코드 입니다.

### 2xx - 성공

200번대의 상태 코드는 대부분 성공을 의미합니다.

- 200 : GET 요청에 대한 성공
- 204 : No Content. 성공했으나 응답 본문에 데이터가 없음
- 205 : Reset Content. 성공했으나 클라이언트의 화면을 새로 고침하도록 권고
- 206 : Partial Conent. 성공했으나 일부 범위의 데이터만 반환

### 3xx - 리다이렉션

300번대의 상태 코드는 대부분 클라이언트가 이전 주소로 데이터를 요청하여 서버에서 새 URL로 리다이렉트를 유도하는 경우입니다.

- 301 : Moved Permanently, 요청한 자원이 새 URL에 존재
- 303 : See Other, 요청한 자원이 임시 주소에 존재
- 304 : Not Modified, 요청한 자원이 변경되지 않았으므로 클라이언트에서 캐싱된 자원을 사용하도록 권고. [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag)와 같은 정보를 활용하여 변경 여부를 확인

### 4xx - 클라이언트 에러

400번대 상태 코드는 대부분 클라이언트의 코드가 잘못된 경우입니다. 유효하지 않은 자원을 요청했거나 요청이나 권한이 잘못된 경우 발생합니다. 가장 익숙한 상태 코드는 404 코드입니다. 요청한 자원이 서버에 없다는 의미죠.

- 400 : Bad Request, 잘못된 요청
- 401 : Unauthorized, 권한 없이 요청. Authorization 헤더가 잘못된 경우
- 403 : Forbidden, 서버에서 해당 자원에 대해 접근 금지
- 405 : Method Not Allowed, 허용되지 않은 요청 메서드
- 409 : Conflict, 최신 자원이 아닌데 업데이트하는 경우. ex) 파일 업로드 시 버전 충돌

### 5xx - 서버 에러

500번대 상태 코드는 서버 쪽에서 오류가 난 경우입니다.

- 501 : Not Implemented, 요청한 동작에 대해 서버가 수행할 수 없는 경우
- 503 : Service Unavailable, 서버가 과부하 또는 유지 보수로 내려간 경우

<br>

## HTTP 프로토콜 특징

HTTP의 특징으로는 **상태가 없는(stateless**) 프로토콜입니다. 여기서 상태가 없다라는 말은 각각의 데이터 주고받기를 위한 요청이 서로 독립 적으로 관리가 된다는 말입니다. 좀 더 쉽게 말해서 이전 데이터요청과 다음 데이터 요청이 서로 관련이 없다는 말이죠.

- 이러한 특징 덕분에 서버는 세션과 같은 별도의 추가 정보를 관리하지 않아도 되고, 다수의 요청 처리 및 서버의 부하를 줄일 수 있는 성능 상의 이점이 생깁니다.

- 하지만 연결을 끊어버리기 때문에, 클라이언트의 이전 상태를 알 수가 없다. 이러한 HTTP의 stateless 특성으로 Connectionless 로 부터 파생되는 특징이라고 할 수 있다. 클라이언트의 이전 상태 정보를 알 수 없게 되면, 웹 서비스를 하는데 당장에 문제가 생긴다.
  클라이언트가 과거에 로그인을 성공하더라도 로그 정보를 유지할 수가 없다. HTTP는 cookie를 이용해서 이 문제를 해결하고 있다.

- Cookie는 클라이언트와 서버의 상태 정보를 담고 있는 정보조각이다. 로그인을 예로 들자면, 클라이언트가 로그인에 성공하면, 서버는 로그인 정보를 자신의 데이터베이스에 저장하고 동일한 값을 cookie형태로 클라이언트에 보낸다.

첫 요청 시 :

- 클라이언트 로그인 성공 then 서버 로그인정보를 자신의 DB에 저장 (서버는 cookie를 키로하는 값을 데이터베이스에 저장하는 방식으로 "세션"을 유지한다) and then return 쿠키 to 클라이언트
- 클라이언트는 다음 번 요청때 cookie를 서버에 보내는데, 서버는 cookie 값으로 자신의 데이터베이스를 조회해서 로그인 여부를 확인할 수 있다.

두번쨰 요청 시 :

- 클라이언트 request(cookie) to server then 서버는 자신의 DB 조회 and then 로그인여부 확인

<br>

## URL

URL(Uniform Resource Locators)은 서버에 자원을 요청하기 위한 주소입니다.

구조로는 밑에 보이시는 것과 같습니다.

![url](https://user-images.githubusercontent.com/58774316/111725108-cc196900-88a9-11eb-93a8-75c12922659a.png)
