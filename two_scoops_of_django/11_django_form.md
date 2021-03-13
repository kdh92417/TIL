# 11. 장고 폼의 기초

```python
import json

from django.contrib import messages
from django.core    import serializers
from core.models    import ModelFormFailureHistory

class FlavorActionMixin(object):

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(FlavorActionMixin, self).form_valid(form)

    def form_invalid(self, form):
        """실패 내역을 확인하기 위해 유효성 검사에 실패한 폼과 모델을 저장한다."""
        form_data = json.dumps(form.cleaned_data)
        model_data = serializers.serialize("json", [form.instance])[1:-1]

        ModelFormFailureHistory.objects.create(
            form_data = form_data,
            model_data = model_data
        )
        return super(FlavorActionMixin, self).form_invalid(from)
```

<br>

## @property

- private한 속성값을 가져올 때 get, set을 쓰는데 Python에서는 @property 데코레이터를 이용하여 get, set 메소드보다 직관적으로 표현이 가능하다.

### Get, Set

```python
class Person :

    def __init__(self):
        self.__name = 'hong'

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
```

### @property

```python
class Person :

    def __init__(self):
        self.__name = 'hong'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

person = Person()
print(person.name)    # hong
person.name = 'park'
print(person.name)    # park
```

<br>

### super()

- https://leemoney93.tistory.com/37

<br>

## 에러 부분

```python
from django import forms

class IceCreamReviewForm(forms.Form):
    # tester 폼의 나머지 부분이 이곳에 위치

    def clean(self):
        cleaned_data = super(TasterForm, self).clean()
        flavor = cleaned_data.get("flavor")
        age = cleaned_data.get("age")

        if flavor == 'coffee' and age < 3:
            # 나중에 보여줄 에러들을 기록
            msg = "Coffee Ice Cream is not for Babies."
            self.add_error('flavor', msg)
            self.add_error('age', msg)

        # 항상 처리된 데이터 전체를 반환한다.
        return cleaned_data

```
