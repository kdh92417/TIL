## Component

---

> 화면의 구조를 모듈별로 나눈 것

- component.vue 의 구조
    - HTML ( Template)
    - JS ( scripts )
    - CSS ( style )
    
<br>
<br>

## Component  구현

---

### 1. FormComponent  구현

- index.html
    
    ```html
    <form>
      <input type="text" placeholder="검색어를 입력하세요" autofocus>
      <button type="reset" class="btn-reset"></button>
    </form>
    
    <template id="search-form">
      <form v-on:submit.prevent="onSubmit">
        <input type="text" v-model="inputValue" v-on:keyup="onKeyup" placeholder="검색어를 입력하세요" autofocus>
        <button v-show="inputValue.length" v-on:click="onReset" type="reset" class="btn-reset"></button>
      </form>
    </template>
    ```
    
                                                                              ⬇️
    
    ```html
    <search-form v-bind:value="query" v-on:@submit="onSubmit"
            v-on:@reset="onReset"></search-form>
    ```
    

- FormComponent.js
    
    ```jsx
    export default {
        template: '#search-form',
        props: ['value'],
        data() {
            return {
                inputValue: this.value
            }
        },
        methods: {
            onSubmit() {
                this.$emit('@submit', this.inputValue.trim())
            },
            onKeyup() {
                if (!this.query.length) this.onReset()
            },
            onReset() {
                this.inputValue = ''
                this.$emit('@reset')
            }
        }
    }
    ```
    

- app.js
    
    ```jsx
    import FormComponent from './components/FormComponent.js'
    
    components: {
      'search-form': FormComponent,
    }
    ```

<br>