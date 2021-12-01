- [Vanilla Javascript](#vanilla-javascript)
    + [1. `1-vanilla/scafolding`](#1--1-vanilla-scafolding-)
    + [2. `1-vanilla/controller`](#2--1-vanilla-controller-)
    + [3.  `1-vanilla/FormView1`](#3---1-vanilla-formview1-)
    + [4.  `1-vanilla/FormView3` : X 버튼을 클릭하거나, 검색어를 삭제하면 검색 결과를 삭제](#4---1-vanilla-formview3----x-------------------------------)
    + [5.  `1-vanilla/FormView4` : 검색결과 구현 1](#5---1-vanilla-formview4------------1)
    + [6.  `1-vanilla/ResultView1` : 검색 결과가 보인다.](#6---1-vanilla-resultview1--------------)
    + [7.  `1-vanilla/ResultView2` : `X` 버튼을 클릭하면 검색폼이 초기화 되고, 검색 결과가 사라진다.](#7---1-vanilla-resultview2-----x-----------------------------------)
    + [8.  `1-vanilla/ResultView3` : 추천 검색어, 최근 검색어 탭이 검색폼 아래 위치한다.](#8---1-vanilla-resultview3---------------------------------)
    + [9.  `1-vanilla/TabView1` : 기본으로 추천 검색어 탭을 선택한다.](#9---1-vanilla-tabview1-----------------------)
    + [10. `1-vanilla/TabView2` : 각 탭을 클릭하면 탭 아래 내용이 변경된다.](#10--1-vanilla-tabview2---------------------------)
    + [11. `1-vanilla/TabView3` : 최근 검색어, 목록이 탭 아래 위치한다.](#11--1-vanilla-tabview3-------------------------)
    + [12. `1-vanilla/KeywordView1` :목록에서 검색어를 클릭하면 선택된 검색어로 검색 결과 화면으로 이동](#12--1-vanilla-keywordview1----------------------------------------)
    + [13. `1-vanilla/KeywordView2` : 검색폼에 선택된 추천 검색어 설정](#13--1-vanilla-keywordview2----------------------)
    + [14. `1-vanilla/KeywordView3` : 최근 검색어, 목록이 탭 아래 위치한다.](#14--1-vanilla-keywordview3-------------------------)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Vanilla Javascript

### 1. `1-vanilla/scafolding`

- 컨트롤러 맛보기

<br>

### 2. `1-vanilla/controller`

- FormView : 검색창에 입력하면 `x` 버튼 사라지게 만들기
    
    ```javascript
    // index.html
    
    <script type="module" src="./js/app.js"></script>
    ```
    
    ```javascript
    // app.js
    
    import MainController from './controllers/MainController.js'
    
    document.addEventListener('DOMContentLoaded', () => {
      MainController.init()
    })
    ```
    
    ```javascript
    // MainController.js
    import FormView from '../views/FormView.js';
    
    const tag = '[MainController]'
    
    export default {
      init() {
        console.log(tag, 'init()');
        FormView.setup(document.querySelector('form'))
      }
    }
    ```
    
    ```javascript
    import View from './View.js';
    
    const tag = '[FormView]'
    
    // FormView 객체에 View 객체의 메소드를 추가
    const FormView = Object.create(View)
    
    FormView.setup = function (el) {
        // el 인자를 받도록 강제
        this.init(el)
        this.inputEl = el.querySelector('[type=text]')
        this.resetEl = el.querySelector('[type=reset]')
        this.showResetBtn(false)
    }
    
    FormView.showResetBtn = function (show = true) {
        this.resetEl.style.display = show ? 'block' : 'none';
    }
    
    export default FormView;
    ```

<br>

### 3.  `1-vanilla/FormView1`

- 입력창에 입력하면 `X` 버튼 보이게 하기
    
    ```javascript
    import View from './View.js'
    
    const tag = '[FormView]'
    
    const FormView = Object.create(View)
    
    FormView.setup = function (el) {
      this.init(el)
      this.inputEl = el.querySelector('[type=text]');
      this.resetEl = el.querySelector('[type=reset]');
      this.showResetBtn(false);
      this.bindEvents();
      return this
    }
    
    FormView.showResetBtn = function (show = true) {
      this.resetEl.style.display = show ? 'block' : 'none';
    }
    
    // 여기서 부터 작업
    FormView.bindEvents = function() {
      // keyup Event : 키를 놓을 때 발생
      this.inputEl.addEventListener('keyup', e => this.onKeyup(e));
    }
    
    FormView.onKeyup = function () {
      this.showResetBtn(this.inputEl.value.length);
    }
    
    export default FormView
    ```
    
<br>

### 4.  `1-vanilla/FormView3` : X 버튼을 클릭하거나, 검색어를 삭제하면 검색 결과를 삭제

- FormView.js
    
    ```javascript
    
    FormView.bindEvents = function () {
      this.on('submit', e => e.preventDefault())
      this.inputEl.addEventListener('keyup', e => this.onKeyup(e))
    
      // X버튼 Click Events
      this.resetEl.addEventListener('click', e => this.onClickReset())
    }
    
    FormView.onKeyup = function (e) {
      const enter = 13
      this.showResetBtn(this.inputEl.value.length)
    
    	// 검색한 값을 다 지웠을 때 X버튼 클릭한 것과같은 이벤트 발생
      if (!this.inputEl.value.length) this.emit('@reset')
      if (e.keyCode !== enter) return
      this.emit('@submit', { input: this.inputEl.value })
      this.inputEl.value = '';
    }
    
    // MainController에게 x버튼 눌렀다고 알리고, 버튼 사라지게 하기
    FormView.onClickReset = function () {
      this.emit('@reset')
      this.showResetBtn(false)
    }
    
    export default FormView
    ```
    

- MainController.js
    
    ```javascript
    import FormView from '../views/FormView.js'
    
    const tag = '[MainController]'
    
    export default {
      init() {
        FormView.setup(document.querySelector('form'))
          .on('@submit', e => this.onSubmit(e.detail.input))
          .on('@reset', e => this.onResetForm())  // 리셋버튼이 눌러졌을 때 FormView에서 전달받음
      },
      
      onSubmit(input) {
        console.log(tag, 'onSubmit()', input)
      },
    
      onResetForm() {
        console.log(tag, 'onResetForm()')
      }
    }
    ```
    
<br>

### 5.  `1-vanilla/FormView4` : 검색결과 구현 1

- ResultView.js
    
    ```javascript
    import View from './View.js';
    
    const tag = '[ResultView]'
    
    const ResultView = Object.create(View)
    
    // DOM 요소를 가진 ResultView 객체로 초기화
    ResultView.setup = function (el) {
        this.init(el);
    }
    
    // 검색값이 있는지 없는지 조회 있다면 getSearchResultsHtml() 함수 실행
    ResultView.render = function(data = []) {
        console.log(tag, 'render()', data);
        this.el.innerHTML = data.length ? this.getSearchResultsHtml(data) : 'There are no search results.';
    }
    
    ResultView.getSearchResultsHtml = function (data) {
        debugger
    }
    
    export default ResultView;
    ```
    

- SearchModel.js
    
    ```javascript
    const data = [
      {
        id: 1,
        name: '[키친르쎌] 홈메이드 칠리소스 포크립 650g',
        image: 'https://cdn.bmf.kr/_data/product/H1821/5a4ed4e8a6751cb1cc089535c000f331.jpg'
      },
      {
        id: 2,
        name: '[키친르쎌] 이탈리아 파티 세트 3~4인분',
        image: 'https://cdn.bmf.kr/_data/product/H503E/300d931e3b8252ed628b6a3c2f56936b.jpg'
      }
    ]
    
    // Promise 객체로 data 넘겨줌
    export default {
      list(query) {
        return new Promise(res => {
          setTimeout(()=> {
            res(data)
          }, 200);
        })
      }
    }
    ```
    

- MainController.js
    
    ```javascript
    
    export default {
      init() {
        FormView.setup(document.querySelector('form'))
          .on('@submit', e => this.onSubmit(e.detail.input))
          .on('@reset', e => this.onResetForm())
    
    		// 0. 검색창 ResultView로 초기화
        ResultView.setup(document.querySelector('#search-result'))
      },
    
    	// 2. 모델을 통해 데이터를 받아온다.
      search(query) {
        console.log(tag, 'search()', query);
        SearchModel.list(query).then(data => {
          this.onSearchResult(data);
        })
      
      },
    	
    	// 1. 검색값을 넘겨받아 search(검색값) 실행
      onSubmit(input) {
        console.log(tag, 'onSubmit()', input);
        this.search(input);
      },
    
    	// 3. 검색결과 렌더링
      onSearchResult(data) {
        ResultView.render(data);
      }
    }
    ```
    

### 6.  `1-vanilla/ResultView1` : 검색 결과가 보인다.

- ResultView.js
    
    ```javascript
    import View from './View.js'
    
    const tag = '[ResultView]'
    
    const ResultView = Object.create(View)
    
    ResultView.messages = {
      NO_RESULT: '검색 결과가 없습니다'
    }
    
    ResultView.setup = function (el) {
      this.init(el)
    }
    
    ResultView.render = function (data = []) {
      console.log(tag, 'render()', data)
      this.el.innerHTML = data.length ? this.getSearchResultsHtml(data) : this.messages.NO_RESULT
      this.show()
    }
    
    // reduce 메소드를 이용하여 img와 검색결과값을 포함한 html를 만들어 반환
    ResultView.getSearchResultsHtml = function (data) {
        return data.reduce((html, item) => {
            html += this.getSearchItemHtml(item)
            return html
        }, '<ul>') + '</ul>'
    }
    
    // Item에 있는 이미지 주소와 검색결과값 추출하여 엘리먼트 요소로 만듬
    ResultView.getSearchItemHtml = function (item) {
        return `<li>
            <img src="${item.image}">
            <p>${item.name}</p>
        </li>`
    }
    
    export default ResultView
    ```
    
<br>

### 7.  `1-vanilla/ResultView2` : `X` 버튼을 클릭하면 검색폼이 초기화 되고, 검색 결과가 사라진다.

- MainController.js
    
    ```javascript
    onResetForm() {
        console.log(tag, 'onResetForm()')
        ResultView.hide();  // 검색결과를 숨겨준다 (View의 method)
    },
    ```

<br> 

### 8.  `1-vanilla/ResultView3` : 추천 검색어, 최근 검색어 탭이 검색폼 아래 위치한다.

- index.html
    
    ```html
    <div class="content">
      <ul id="tabs" class="tabs">
        <li>추천 검색어</li>
        <li>최근 검색어</li>
      </ul>
      <div id="search-result"></div>
    </div>
    ```

<br>
    

### 9.  `1-vanilla/TabView1` : 기본으로 추천 검색어 탭을 선택한다.

- TabView.js
    
    ```javascript
    import View from "./View.js";
    
    const tag = '[TabView]'
    
    const TabView = Object.create(View)
    
    TabView.setup = function (el) {
        this.init(el)
    }
    
    // 선택된 탭의 li 클래스네임을 activate로 바꾼다.
    TabView.setActiveTab = function (tabName) {
        Array.from(this.el.querySelectorAll('li')).forEach(li => {
            li.className = li.innerHTML === tabName ? 'active' : ''
        })
    }
    
    export default TabView
    ```
    

- MainController.js
    
    ```javascript
    
    import TabView from '../views/TabView.js'
    
    export default {
      init() {
        FormView.setup(document.querySelector('form'))
          .on('@submit', e => this.onSubmit(e.detail.input))
          .on('@reset', e => this.onResetForm())
    
    		// TabView 초기화
        TabView.setup(document.querySelector('#tabs'))
    
        ResultView.setup(document.querySelector('#search-result'))
    
    		// 초기 탭은 '추천 검색어' 로 고정
        this.selectedTab = '추천 검색어';
    
    		// 선택된 탭 그리기
        this.renderView();
      },
    
      renderView() {
        console.log(tag, 'renderView()')
        TabView.setActiveTab(this.selectedTab);
        ResultView.hide();
      },
    }
    ```
    
<br>

### 10. `1-vanilla/TabView2` : 각 탭을 클릭하면 탭 아래 내용이 변경된다.

- TabView.js
    
    ```javascript
    import View from './View.js'
    
    const tag = '[TabView]'
    
    const TabView = Object.create(View)
    
    TabView.tabNames = {
      recommand: '추천 검색어',
      recent: '최근 검색어',
    }
    
    // TabView 초기화 할때 각 li 요소에 click 이벤트를 바인딩
    TabView.setup = function (el) {
      this.init(el);
      this.bindClick();
      return this
    }
    
    TabView.bindClick = function () {
        Array.from(this.el.querySelectorAll('li')).forEach(li => {
            li.addEventListener('click', () => this.onClick(li.innerHTML))
        })
    }
    
    // 해당 li 클래스를 active로 바꾸고 MainController에게 알린다.
    TabView.onClick = function (tabName) {
        this.setActiveTab(tabName)
        this.emit('@change', {tabName})
    }
    
    TabView.setActiveTab = function (tabName) {
      Array.from(this.el.children).forEach(li => {
        li.className = li.innerHTML === tabName ? 'active' : ''
      })
      this.show()
    }
    
    export default TabView
    ```
    

- MainController.js
    
    ```javascript
    
    export default {
      init() {
        FormView.setup(document.querySelector('form'))
          .on('@submit', e => this.onSubmit(e.detail.input))
          .on('@reset', e => this.onResetForm())
    
        TabView.setup(document.querySelector('#tabs'))
    			// tab 변경될때 이벤트를 받는다.
          .on('@change', e => this.onChangeTab(e.detail.tabName))
    
        ResultView.setup(document.querySelector('#search-result'))
    
        this.selectedTab = '추천 검색어';
        this.renderView();
      },
    
      onChangeTab(tabName) {
        debugger
      },
      
      
    }
    ```

<br>
    

### 11. `1-vanilla/TabView3` : 최근 검색어, 목록이 탭 아래 위치한다.

- KeywordView.js
    
    ```javascript
    import View from "./View.js";
    
    const tag = '[KeywordView]'
    
    const KeywordView = Object.create(View)
    
    // Keyword DOM요소 초기화
    KeywordView.setup = function (el) {
      this.init(el)
    }
    
    // 화면에 키워드모델 데이터 표시
    KeywordView.render = function (data = []) {
        this.el.innerHTML = data.length ? this.getKeywordsHtml(data) : 'There is no recommended search word'
        this.show()
    }
    
    // KeywordModel DATA -> html element 로 변환
    KeywordView.getKeywordsHtml = function (data) {
        return data.reduce((html, item, index) => {
            html += `<li>
                <span class="number">${index + 1}</span>
                ${item.keyword}
            </li>`
            return html
        }, '<ul class="list">') + '</ul>'
    }
    
    export default KeywordView
    ```
    

- MainController.js
    
    ```javascript
    import FormView from '../views/FormView.js'
    import ResultView from '../views/ResultView.js'
    import TabView from '../views/TabView.js'
    import KeywordView from '../views/KeywordView.js'
    
    import SearchModel from '../models/SearchModel.js'
    import KeywordModel from '../models/KeywordModel.js'
    
    const tag = '[MainController]'
    
    export default {
      init() {
        FormView.setup(document.querySelector('form'))
          .on('@submit', e => this.onSubmit(e.detail.input))
          .on('@reset', e => this.onResetForm())
    
        TabView.setup(document.querySelector('#tabs'))
          .on('@change', e => this.onChangeTab(e.detail.tabName))
    
        KeywordView.setup(document.querySelector('#search-keyword'))
        ResultView.setup(document.querySelector('#search-result'))
    
        this.selectedTab = '추천 검색어'
        this.renderView()
      },
    
      renderView() {
        console.log(tag, 'rednerView()')
        TabView.setActiveTab(this.selectedTab)
    
    		// Keyword Data 가져오기
        if (this.selectedTab === '추천 검색어') {
          this.fetchSearchKeyword();
        } else {
    			
        }
    	
        ResultView.hide()
      },
    	// Keyword DATA 가져온뒤 Display
      fetchSearchKeyword() {
        KeywordModel.list().then(data => {
          KeywordView.render(data)
        })
        
      },
    
    }
    ```

<br>
    

### 12. `1-vanilla/KeywordView1` :목록에서 검색어를 클릭하면 선택된 검색어로 검색 결과 화면으로 이동

- KeywordView.js
    
    ```javascript
    // bindClickEvent() 메소드를 setup -> render안에서 호출 : 메소드의 키워드 데이터받고나서 호출하도록 변경
    KeywordView.render = function (data = []) {
      this.el.innerHTML = data.length ? this.getKeywordsHtml(data) : this.messages.NO_KEYWORDS;
      this.bindClickEvent();  // <-
      this.show()
    }
    ```
    
    ```javascript
    // 각 키워드 li 요소에 click event 바인딩
    KeywordView.bindClickEvent = function () {
        Array.from(this.el.querySelectorAll('li')).forEach(li => {
            li.addEventListener('click', e => this.onClickKeyword(e))
        })
    }
    
    // MainController에 click event 보냄
    KeywordView.onClickKeyword = function (e) {
        const { keyword } = e.currentTarget.dataset
        this.emit('@click', {keyword})
    }
    ```
    
<br>

### 13. `1-vanilla/KeywordView2` : 검색폼에 선택된 추천 검색어 설정

- MainController.js
    
    ```javascript
    
    search(query) {
    	// 키워드값을 설정하는 setValue 메소드실행
    	FormView.setValue(query);
    	SearchModel.list(query).then(data => {
          this.onSearchResult(data)
      })
    },
    ```
    
- FormView.js
    
    ```javascript
    // 검색창을 인풋값으로 설정
    FormView.setValue = function (value = '') {
      this.inputEl.value = value;
      this.showResetBtn(this.inputEl.value.length);
    }
    ```
    

- onResetForm()
    
    ```javascript
    onResetForm() {
        console.log(tag, 'onResetForm()')
        // ResultView.hide()
        this.renderView(); // <- 검색결과를 숨기는 게 아니라 탭뷰를 그리도록 호출
      },
    ```
    
<br>

### 14. `1-vanilla/KeywordView3` : 최근 검색어, 목록이 탭 아래 위치한다.

- HistoryView.js
    
    ```javascript
    // KeywordView와 기능이 같아 KeywordView 객체를 복사하여 사용
    import KeywordView from "./KeywordView.js";
    
    const tag = '[HistoryView]';
    
    const HistoryView = Object.create(KeywordView)
    
    export default HistoryView;
    ```
    

- MainController.js
    
    ```javascript
    
    export default {
      init() {
        // KeywordView 객체와 똑같이 초기화 & 이벤트 바인딩
        HistoryView.setup(document.querySelector('#search-keyword'))
          .on('@click', e => this.onClickHistory(e.detail.keyword))
    
    		// 초기 탭 '최근 검색어' 로 변경
        this.selectedTab = '최근 검색어'
        this.renderView()
      },
    
      renderView() {
        console.log(tag, 'rednerView()')
        TabView.setActiveTab(this.selectedTab)
        
        if (this.selectedTab === '추천 검색어') {
          this.fetchSearchKeyword();
        } else {
    		  // 최근검색 데이터 가져옴
          this.fetchSearchHistory();
        }
    
        ResultView.hide();
      },
    
      fetchSearchHistory() {
        HistoryModel.list().then(data => {
          HistoryView.render(data);
        })
      },
    }
    ```
