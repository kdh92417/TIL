## 목차

- [Vue.js MVVM Pattern](#vuejs-mvvm-pattern)
  * [MVVM (Model - View - ViewModel )](#mvvm--model---view---viewmodel--)
- [실습](#--)
  * [1. 검색폼 구현](#1-검색폼-구현)
  * [2. 검색결과 구현](#2-검색결과-구현)
  * [3. 탭 구현](#3-탭-구현)
  * [4. 추천 검색어 구현](#4-추천-검색어-구현)
  * [5. 최근 검색어 구현](#5-최근-검색어-구현)

<br>

## Vue.js MVVM Pattern

---

### MVVM (Model - View - ViewModel )

- ViewModel : `Model` 과 `View` 사이에 위치해서 `Model` 로 부터 데이터를 가져와서 `View`  적합한 데이터로 가공한다. 그리고 데이터가 바뀔 때마다 `ViewModel`  에 연결되어있는 `View` 도 같이 반영되어진다.

- Console Ex)
    
    ```javascript
    const h1 = document.createElement('h1');
    //undefined
    
    document.body.appendChild(h1);
    //<h1></h1>
    
    const viewModel = {}
    // undefined
    
    let model = '';
    // undefined
    
    Object.defineProperty(viewModel, 'model', {
        get() { return model; },
        set(val) {
            model = val;
            h1.innerHTML = model;
        }
    });
    // {}
    
    viewModel.model
    // ''
    
    viewModel.model = 'hello world';
    // 'hello world' <- 화면에 즉각 반영 ( ViewModel )
    
    viewModel.model = 'Adam';
    // 'Adam' <- 화면에 즉각 반영 ( ViewModel )
    ```

<br>
<br>

## 실습

---

### 1. 검색폼 구현

1. 검색 상품명 입력 폼이 위치한다. 검색어가 없는 경우이므로 x 버튼을 숨긴다.
2. 검색어를 입력하면  x버튼이 보인다.
3. 엔터를 입력하면 검색 결과가 보인다. (컨트롤러에게 위임)
4. x 버튼을 클릭하거나, 검색어를 삭제하면 검색 결과를 삭제한다. (실습)

- index.html
    
    ```html
    	<div id="app">
        <header>
          <h2 class="container">검색</h2>
        </header>
    
        <div class="container">
    			<!-- v-on 디텍티브를 이용하여 onSubmit 함수로 이벤트 바인딩 -->
          <form v-on:submit.prevent="onSubmit">
    				<!-- v-on 디텍티브를 이용하여 onKeyup 함수로 이벤트 바인딩 -->
            <input type="text" v-model="query" v-on:keyup="onKeyup" placeholder="검색어를 입력하세요" autofocus>
    				<!-- v-show를 이용하여 검색값이 있을 때만 보여주기 -->
            <button v-show="query.length" v-on:click="onReset" type="reset" class="btn-reset"></button>
          </form>
        </div>
      </div>
    ```
    

- app.js
    
    ```javascript
    new Vue({
      el: '#app',
      data: {
        query: ''
      },
      methods: {
          onSubmit(e) {
            debugger
          },
          
          onReset() {
            this.query = '';
            //  검색결과를 숨기는 ...
            debugger
          },
    
          onKeyup() {
            if (!this.query.length) this.onReset()
          }
      }
    
    })
    ```
    

- branch : `2-vue-install` , `2-vue/Form1`
- v-model : 양방향 데이터 바인딩
- v-show() : 해당 요소를 보여줄지 않을지 정하는 메소드

<br> 

### 2. 검색결과 구현

- branch : `2-vue/Form2` , `2-vue/Result1`

1. 검색 결과가 검색폼 아래 위치한다.
2. 검색 결과가 보인다.
3. x버튼을 클릭하면 검색폼이 초기화 되고, 검색 결과가 사라진다.

- index.html
    
    ```javascript
    <div v-if="submitted">
      <div v-if="searchResult.length">
        <ul>
          <li v-for="item in searchResult">
            <img v-bind:src="item.image"> {{ item.name }}
          </li>
        </ul>
      </div>
    
      <div v-else>
        {{ query }} 검색어로 찾을 수 없습니다.
      </div>
    </div>
    ```
    

- app.js
    
    ```javascript
    methods: {
      // 검색 이벤트일때  search 이벤트 바인딩
    	onSubmit(e) {
        this.search()
      },
      
    	// 검색값을 다지웠을 때 restForm 이벤트 바인딩
      onKeyup(e) {
        if (!this.query.length) this.resetForm()
      },
    
    	// X 버튼 클릭했을 때 resetForm 이벤트 바인딩
      onReset(e) {
        this.resetForm()
      },
    
      search() {
          SearchModel.list().then(data => {
    					// 검색 값 입력할 때가 아니라 검색할 때
              this.submitted = true;
    
    					//  프로미스로 받아온 데이터를  searchResult 에 할당
              this.searchResult = data;
          })
      },
      resetForm() {
        this.query = '';
    
    		// 검색값이 reset 되어졌을 때 결과 값 없애기 위해 submitted  & searchResult 초기화
        this.submitted = false;
        this.searchResult = [];
      }
    }
    ```

<br>    

### 3. 탭 구현

- branch : `2-vue/Result2`

1. 추천 검색어, 최근 검색어 탭이 검색폼 아래 위치한다.
2. 기본으로 추천 검색어 탭을 선택한다.
3. 각 탭을 클릭하면 탭 아래 내용이 변경된다.

- index.html
    
    ```html
    <div v-else>
      <ul class="tabs">
    		<!-- tabs의 요소중 selectedTab 인 것만 active 하고 각 탭에 click 이벤트 바인딩 -->
        <li v-for="tab in tabs" v-bind:class="{active: tab === selectedTab}" 
            v-on:click="onClickTab(tab)">
          {{ tab }}
        </li>
      </ul>
    
    	<!-- 해당 탭에해당하는 검색결과값 rending -->
      <div v-if="selectedTab === tabs[0]">
        추천 검색어 목록
      </div>
      <div v-else>
        최근 검색어 목록
      </div>
    </div>
    ```
    

- app.js
    
    ```javascript
    new Vue({
      el: '#app',
      data: {
        query: '',
        submitted: false,
        tabs: ['추천 검색어', '최근 검색어'],
        selectedTab : '',
        searchResult: [],
      },
    	// created 라이프사이클일 때 : '추천 검색어' 탭으로 디폴트
      created() {
        this.selectedTab = this.tabs[0]
      },
      methods: {
        .
        .
        .
    		// 탭이 클릭될때 해당 탭으로 active
        onClickTab(tab) {
          this.selectedTab = tab;
        },
    
    		// 검색할 때 결과값 가져오기
        search() {
          SearchModel.list().then(data => {
            this.submitted = true
            this.searchResult = data
          })
        },
        
      }
    })
    ```
    
<br>

### 4. 추천 검색어 구현

1. 번호, 추천 검색어 목록이 탭 아래 위치한다.
2. 목록에서 검색어를 클릭하면 선택된 검색어로 검색 결과 화면으로 이동
3. 검색폼에 선택된 추천 검색어 설정

- branch : `2-vue/TabView2`

- index.html
    
    ```html
    <div v-if="selectedTab === tabs[0]">
      <div v-if="keywords.length">
        <ul class="list">
          <li v-for="(item, index) in keywords" 
              v-on:click="onClickKeyword(item.keyword)">
            <span class="number">{{ index+1 }}</span>
            {{ item.keyword }}
          </li>
        </ul>
      </div>
    </div>
    ```
    

- app.js
    
    ```javascript
    data: {
    	.
    	.
    	keywords: []
    },
    methods: {
    	// Keyword 데이터 가져오기
    	fetchKeyword() {
        KeywordModel.list().then(data => {
          this.keywords = data
        })
      },
    
    	// 추천 검색어 클릭시 검색결과 나타나게 하고, 검색창에 해당 클릭값 바인딩
    	onClickKeyword(keyword) {
    		this.query = keyword
    		this.search()
    	}
    }
    ```
    
<br>

### 5. 최근 검색어 구현

1. 최근 검색어, 목록이 탭 아래 위치한다.
2. 목록에서 검색어를 클릭하면 선택된 검색어로 검색결과 화면으로 이동
3. 검색일자, 버튼 목록이 있다.
4. 목록에서  x 버튼을 클릭하면 선택된 검색어가 목록에서 삭제
5. 검색시마다 최근 검색어 목록에 추가된다.

- index.html
    
    ```html
    <div v-else>
      <div v-if="history.length">
        <ul class="list">
          <li v-for="(item, index) in history" v-on:click="onClickKeyword(item.keyword)">
            {{ item.keyword }}
            <span class="date">{{ item.date }}</span>
    				<!-- stop === stopPropagation() : 버블링이 일어나지 않도록 stop 메소드 -->
            <button class="btn-remove" v-on:click.stop="onRemove(item.keyword)"></button>
          </li>
        </ul>
      </div>
    </div>
    ```
    

- app.js
    
    ```javascript
    created() {
      this.selectedTab = this.tabs[0]
      this.fetchKeyword()
      this.fetchHistory()
    },
    methods: {
    	onRemove(keyword) {
    	  HistoryModel.remove(keyword)
    	  this.fetchHistory()
    	}.
    
    	fetchHistory() {
    	  HistoryModel.list().then(data => {
    	    this.history = data
    	  })
    	},
    
    	search() {
        SearchModel.list().then(data => {
          this.submitted = true
          this.searchResult = data
        })
        HistoryModel.add(this.query)
        this.fetchHistory()
      },
    }
    
    ```