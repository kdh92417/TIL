# Django를 활용하여 서버 구축 및 Ajax를 이용하여 통신해보기

<br>

## Check List

- [x] django를 이용하여 서버구축 완료

- [x] Ajax를 이용하여 클라이언트에서 서버로 데이터 통신

- [x] Ajax를 이용하여 클라이언트에서 서버로 데이터 통신하여 브라우저콘솔에 응답한 데이터 찍히게 하기

<br>

Ajax - GET

```javascript
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.0.0/jquery.min.js"></script>
<script>
    let btnAjax = document.querySelector('#form_button');
    btnAjax.addEventListener('click', e => {
        var tag = document.querySelector('#search').value;
        $.ajax({
            url: "{% url 'search' %}",
            type: 'GET',
            data: { 'tag' : tag },
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

Ajax - POST

```javascript
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.0.0/jquery.min.js"></script>
<script>
    let btnAjax = document.querySelector('#form_button');
    btnAjax.addEventListener('click', e => {
        let paswd = document.querySelector('#paswd').value;
        let name = document.querySelector('#id_name').value;

        let param = {
            'id': name,
            'paswd': paswd,
        }
        $.ajax({
            url: "{% url 'test' %}",
            type: 'POST',
            data: JSON.stringify(param),
            success: function (data) {
                console.log(data);
            },
            error: function () {
                alert('No No');
            }
        })
    });
</script>
```

main/views.py

```python
from django.shortcuts               import render
from django.views.decorators.csrf   import csrf_exempt
from django.http                    import JsonResponse
from django.views                   import View

import json

def index(request):
    return render(request, 'main/index.html')

@csrf_exempt
def login(request):
    return render(request, 'main/login.html')

@csrf_exempt
def test(request):
    json_object = json.loads(request.body)
    print('ID : ',json_object.get('id'))
    print('PASSWORD : ' ,json_object.get('paswd'))
    return JsonResponse(json_object)


def recruit(request):
    template = 'main/recruit.html'
    return render(request, template)


class SearchView(View):
    def get(self, request):
        tag = request.GET.get('tag')
        company_list = {
            'python': ['매스프레소', '휴머스온'],
            'node.js': ['패스트캠퍼스랭귀지', '리디', '딥바이오', '모두싸인'],
            'java': ['투믹스', '리비', '동화기업', '쓰리아이']
        }
        return JsonResponse({'tag' : company_list[tag]})
```
