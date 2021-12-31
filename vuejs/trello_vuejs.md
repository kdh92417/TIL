# 트렐로 개발을 통해 배우는 Vue.js - 인프런

> 인프런 강의에 에있는 [트렐로 개발로 배우는 Vuejs, Vuex, Vue-Router 프론트엔드 실전 기술](https://www.inflearn.com/course/vuejs) 강의를
공부하면서 정리한 내용입니다.

# Table of Contents

- [1. Router](#1-router)
  * [1. 1 Vue Router Install](#1-1-vue-router-install)
    + [npm](#npm)
  * [1.2 Run the router](#12-run-the-router)
  * [1.3 Router modularization](#13-router-modularization)
  * [1.4 Router View](#14-router-view)
    + [Components](#components)
    + [Router](#router)
    + [Root Component](#root-component)
    + [Vue 인스턴스](#vue-----)
  * [1.5 Router Link](#15-router-link)
    + [Navbar Component](#navbar-component)
    + [Root Component](#root-component-1)
    

# 1. Router

## 1. 1 Vue Router Install

- `npm install vue-router`

### npm

- `--save` 옵션
    - package.json 옵션에 dependency 항목에 추가한다는 의미이며 `package.json` 파일만 있다면 패키지를 쉽게 관리할 수 있다는 뜻.
    - npm version 5 이상부터는 기본적으로 `--save` 옵션으로 install 하게 되어있어서 `--save` 옵션을 쓸필요 없음
    
<br>

## 1.2 Run the router

- main.js
    
    ```jsx
    import Vue from 'vue'
    import VueRouter from 'vue-router'
    import App from './App.vue'
    
    Vue.use(VueRouter)
    
    // Components
    const Login = { template: '<div>Login Page</div>' }
    const NotFound = { template: '<div>Page not found</div>' }
    
    // VueRouter인스턴스 생성
    const router = new VueRouter({
    
    	// history mode
      mode: 'history',
      routes: [
        { path: '/', component: App },
        { path: '/login', component: Login },
        { path: '*', component: NotFound }
      ]
    })
    
    new Vue({
      el: '#app',
      router,
      // render(h) {
      //   return h({ template: '<router-view></router-view>' })
      // }
      render: h => h({ template: '<router-view></router-view>' })
    })
    ```
  
<br>    

## 1.3 Router modularization

> router 폴더에 `index.js` 파일을 만들어 라우터 모듈화
> 

- router/index.js
    
    ```jsx
    import Vue from 'vue'
    import VueRouter from 'vue-router'
    import App from '../App.vue'
    
    Vue.use(VueRouter)
    
    const Login = { template: '<div>Login Page</div>' }
    const NotFound = { template: '<div>Page not found</div>' }
    
    const router = new VueRouter({
      mode: 'history',
      routes: [
        { path: '/', component: App },
        { path: '/login', component: Login },
        { path: '*', component: NotFound }
      ]
    })
    
    export default router
    ```
    

- main.js
    
    ```jsx
    import Vue from 'vue'
    import router from './router'
    
    new Vue({
      el: '#app',
      router,
      render: h => h({ template: '<router-view></router-view>' })
    })
    ```

<br>

## 1.4 Router View

> 컴포넌트별로 모듈화하고 `router-view` 를 이용하여 라우팅
> 

### Components

> 컴포넌트별로 모듈화
> 

- components/Home.vue
    
    ```jsx
    <template lang="">
      <div>
        Home Page
      </div>
    </template>
    <script>
    export default {};
    </script>
    <style lang="">
    </style>
    ```
    

- components/Login.vue
    
    ```jsx
    <template lang="">
      <div>
        Login Page
      </div>
    </template>
    <script>
    export default {};
    </script>
    <style lang="">
    </style>
    ```
    
- components/NotFound.vue
    
    ```jsx
    <template lang="">
      <div>
        Page Not Found
      </div>
    </template>
    <script>
    export default {};
    </script>
    <style lang="">
    </style>
    ```
    

### Router

> 컴포넌트 별로 모듈화 한것을 index.js 라우터에서 사용
> 

- router/index.js
    
    ```jsx
    import Vue from 'vue'
    import VueRouter from 'vue-router'
    
    import Home from '../components/Home'
    import Login from '../components/Login'
    import NotFound from '../components/NotFound'
    
    Vue.use(VueRouter)
    
    const router = new VueRouter({
      mode: 'history',
      routes: [
        { path: '/', component: Home },
        { path: '/login', component: Login },
        { path: '*', component: NotFound }
      ]
    })
    
    export default router
    ```
    

### Root Component

> Root Component인 App.vue 렌더링
> 

- App.vue
    
    ```jsx
    <template>
      <div id="app">
        여기서부터 코드를 시작합니다!
        <router-view></router-view>
      </div>
    </template>
    
    <script>
    export default {
      name: "app",
      data() {
        return {};
      },
    };
    </script>
    
    <style>
    
    </style>
    ```
    

### Vue 인스턴스

> Root Component인 App.vue 렌더링
> 

- main.js
    
    ```jsx
    import Vue from 'vue'
    import router from './router'
    import App from './App'
    
    new Vue({
      el: '#app',
      router,
      render: h => h(App)
    })
    ```
    
<br>

## 1.5 Router Link

> `<router-link>`는 다음과 같은 이유로 하드 코드 된 `<a href="...">`보다 선호됩니다.
> 
- HTML5 히스토리 모드와 해시 모드에서 모두 동일한 방식으로 작동하므로 모드를 트랜지션하기로 결정하거나 라우터가 IE9에서 해시 모드로 트랜지션 한 경우 변경할 필요가 없습니다.
- HTML5 히스토리 모드에서, `router-link`는 클릭 이벤트를 차단하여 브라우저가 페이지를 다시 로드하지 않도록합니다.

참조 - [https://router.vuejs.org/kr/api/#router-link](https://router.vuejs.org/kr/api/#router-link)

### Navbar Component

`<router-link>` 를 이용한 링크 처리

- components/Navbar.vue
    
    ```jsx
    <template lang="">
      <div>
        <router-link to="/">Home</router-link>
        <router-link to="/login">Login</router-link>
      </div>
    </template>
    <script>
    export default {};
    </script>
    <style lang="">
    </style>
    ```
    

### Root Component

- App.vue
    
    ```jsx
    <template>
      <div id="app">
        <Navbar />
        <router-view></router-view>
      </div>
    </template>
    
    <script>
    import Navbar from "./components/Navbar";
    
    export default {
      components: { Navbar },
    	.
    	.
    	.
    }
    ```