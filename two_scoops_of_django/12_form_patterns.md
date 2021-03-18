# 폼 패턴들

## 12.1 패턴 1: 간단한 모델폼과 기본 유효성 검사기

```python
from django.views.generic import CreateView, UpdateView
from braces.views         import LoginRequiredMixin
from .models              import Flavor

class Flavor(LoginRequiredMixin, CreateView):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')

class FlavorUpdateView(LoginRequiredMixin, UpdateView):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')
```

<br>

## 12.2 패턴 2 : 모델폼에서 커스텀 폼 필드 유효성 검사기 이용하기

```python
# core/validators.py

from django.core.exceptions import ValidationError


def validate_tasty(value):
    """단어가 'Tasty'로 시작하지 않으면 ValidationError를 일으킨다."""
    if not value.startswitch("Tasty"):
        msg = "Must start with Tasty"
        raise ValidationError(msg)

# 장고에서 커스텀 필드 유효성 검사기는 입력된 인자들이 테스트를 통과하지 못했을 경우 에러를 일으키는 간단한 함수로 되어 있다.
```

### 12.3

```python
# core/models.py
from .validators import validate_tasty
from django.db import models


class TastyTitleAbstractModel(models.Model):
    title = models.Charfield(max_length=255, validator = [validate_tasty])

    class Meta:
        abstract = True
```

### 12.4

```python
# flavors/models.py
from django.urls   import reverse
from django.db     import models

from core.models   import TastyTitleAbstractModel

class Flavor(TastyTitleAbstractModel):
    slug = models.SlugField()
    scoops_remaining = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("flavors:detail", kwargs={"slug": self.slug})
```

### 12.5 - 커스톰 필드 유효성 검사기를 이용하는 커스텀 FlavorForm

```python
# flavor/forms.py
from django     import forms
from django     import validate_tasty
from .models    import Flavor

class FlavorFrom(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].validators.append(validate_tasty)
        self.fields["slug"].validators.append(validate_tasty)

    class Meta:
        model = Flavor
```

### 12.6 입력된 데이터의 유효성을 검사를 위해 FlavorForm을 이용
```python


```