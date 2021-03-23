# Ajax

## Ajax란?

- Ajax는 JavaScript의 라이브러리중 하나이며 Asynchronous Javascript And Xml(비동기식 자바스크립트와 xml)의 약자입니다.
- 브라우저가 가지고있는 XMLHttpRequest 객체를 이용해서 전체 페이지를 새로 고치지 않고도 페이지의 일부만을 위한 데이터를 로드하는 기법 이며 Ajax를 한마디로 정의하자면 **JavaScript를 사용한 비동기 통신, 클라이언트와 서버간에 XML 데이터를 주고받는 기술이라고 할 수 있겠습니다.**

<br>

## 비동기(async) 방식이란?

**비동기 방식은 웹페이지를 리로드하지 않고 데이터를 불러오는 방식입니다.** 이 방식의 장점은 페이지 리로드의 경우 전체 리소스를 다시 불러와야하는데 이미지, 스크립트 , 기타 코드등을 모두 재요청할 경우 불필요한 리소스 낭비가 발생하게 되지만 비동기식 방식을 이용할 경우 필요한 부분만 불러와 사용할 수 있으므로 매우 큰 장점이 있습니다.

<br>

## 왜 사용하는가?

기본적으로 HTTP프로토콜은 클라이언트쪽에서 Request를 보내고 Server쪽에서 Response를 받으면 이어졌던 연결이 끊기게 되어있습니다. 그래서 화면의 내용을 갱신하기 위해서는 다시 request를 하고 response를 하면서 페이지 전체를 갱신하게 됩니다. 하지만 이렇게 할 경우 페이지의 일부분만 갱신할 경우에도 페이지 전체를 다시 로드해야하는데 엄청난 자원낭비와 시간낭비를 초래하고 말것입니다.

하지만 **ajax는 html 페이지 전체가아닌 일부분만 갱신할수 있도록 XML HttpRequest객체를 통해 서버에 request를 합니다. 이 경우 Json이나 xml형태로 필요한 데이터만 받아 갱신하기 때문에 그만큼의 자원과 시간을 아낄 수 있습니다.**

요새 웹페이지에서 가장 중요한것은 속도가 아닐까싶습니다. 이 이유하나만으로도 Ajax를 사용해야 하는 이유로써 충분합니다

<br>

|                                                                    Ajax의 장점                                                                    |                                                                                       Ajax의 단점                                                                                       |
| :-----------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                웹페이지의 속도향상                                                                |                                                                히스토리 관리가 안 된다. (보안에 좀 더 신경을 써야한다.)                                                                 |
|                                             서버의 처리가 완료 될때까지 기다리지 않고 처리 가능하다.                                              |                                                                 연속으로 데이터를 요청하면 서버 부하가 증가할 수 있다.                                                                  |
|                                          서버에서 Data만 전송해면 되므로 전체적인 코딩의 양이 줄어든다.                                           | XMLHttpRequest를 통해 통신을 하는 경우사용자에게 아무런 진행 정보가 주어지지 않는다. <br>그래서 아직 요청이 완료되지 않았는데 사용자가 페이지를 떠나거나 오작동할 우려가 발생하게 된다. |
| 기존 웹에서는 불가능했던 다양한 UI를 가능하게 해준다. <br>사진공유 사이트 Flickr의 경우 사진의 제목이나 태그를 페이지 리로드 없이 수정할 수 있다. |                                             

<br>

## **Jquery와의 시너지**

Ajax하면 Jquery에 대한 설명을 빼놓을 수 없습니다. 일반 Javascript만으로 Ajax를 하게되면 코딩량도 많아지고 브라우저별로 구현방법이 다른 단점이 있는데 jquery를 이용하면 더 적은 코딩량과 동일한 코딩방법으로 대부분의 브라우저에서 같은 동작을 할 수 있게 됩니다.

jquery ajax를 사용하면, HTTP Get방식과 HTTP Post방식 모두를 사용하여 원격 서버로부터 데이터를 요청할 수 있습니다. Jquery는 Ajax처럼 JavaScript의 라이브러리 중 하나인데 자바스크립트를 좀 더 사용하기 쉽게 패키징화 시켜놓은 것입니다. Jquery에대한 내용은 추후에 포스팅하겠습니다.

<br>

## Ajax 사용법

```html
<input type="text" placeholder="기술 태그 검색" id="search" />
<button id="form_button">검색</button>
```

```jsx
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.0.0/jquery.min.js"></script>
<script>
    let btnAjax = document.querySelector('#form_button');
    btnAjax.addEventListener('click', e => {
        var tag = document.querySelector('#search').value;
        $.ajax({
            url: "{% url 'search' %}",
            type: 'GET',
            data: { 'tag' : tag },
						dataType : 'json',
            success: function (data) {
                console.log(data);
            },
            error: function () {
                alert(tag);
            }
        })
    });
</script>
```

### Ajax를 이용하여 통신

- `btnAjax.addEventListener`
  - 검색버튼을 누르면 ID, PASSWORD 값을 변수에 저장하고
  - ajax 호출하여 서버와 통신하게됨
- `$.ajax`
  - url : 요청할 URL 기입
  - type : 통신타입 설정 POST 또는 GET
  - data : 서버에 요청시 보낼 파리미터를 기입(선택사항)
  - dataType : 응답받을 데이터의 타입을 선택(XML, TEXT, HTML, JSON 등)
  - success : 요청 및 응답에 성공하였을 때에 행위를 기입
  - error : 요청 또는 응답에 실패하였을 때에 행위를 기입

**요약하자면**

- 현재위치에서 `search`의 이름을 가진 url에게 `tag` 라는 파라미터를 GET방식으로 요청한다.
- 그러면 `search` url의 주소의 서버는 `tag` 라는 파라미터를 받고 클라이언트(ajax)에게 response 한다.
- 위의 success에서는 서버에서 response 해준 data를 브라우저 콘솔에 찍히게 만들었다.
