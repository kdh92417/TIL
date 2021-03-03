3. [Django Basics](#-chpater-3-django-basics)
4. [Templates and Media Files](#-chapter-4-templates-and-media-files)
5. [Models and Databases](#-chapter-5-models-and-databases)

<br>

# Chapter 3 Django Basics

### 장고 프로젝트 생성하기

> `django-admin startproject <name>`

- 장고 프로젝트 생성하는 명령어 이고 `<name>` 에는 원하는 프로젝트 넣으면 된다.

### Django App 생성하기

1. `python manage.py startapp <name>`

   - 새로운 장고앱을 생성하기 위한 명령어
   - `manage.py` 파일이 있는 프로젝트 폴더 내에서 쳐야된다.
   - `<name>` 에는 원하는 앱 이름을 넣으면 된다.

2. App을 생성하였으면 Django에게 App을 생성하였다고 알려줘야된다.

   - project 폴더 내에있는 settings.py 파일에 INSTALLED_APPS 항목에 앱 이름을 추가시킨다.

3. project 폴더 내에 urls.py파일에서 맵핑하는 것을 앱에게 추가합니다.

   - `path`, `url` 방식이 있다.

4. App 디텍터리에 urls.py를 만들어 들어오는 url 문자열을 view로 지정한다.

5. App의 view.py에서 필요한 view를 만들어 HttpResponse object를 반환한다.

<br>
<br>

# Chapter 4. Templates and Media Files

- Templaes 폴더를 manage.py에 있는 곳에 생성

  - 하위폴더는 각앱별로 생성 : 이래야 어떤앱의 템플릿인지 앎

- [Settings.py](http://settings.py) 에 템플릿을 추가했다고 알려줘야되는데 절대경로로 추가하면안됨 → 다른사람과 같이 프로젝트를 진행할 시 다른사람과의 경로가 맞지 않음

  - 그래서 상대경로를 이용해야함

- TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

```python
# 해당 컴퓨터 에서 해당 디텍토리 절대경로를 저장
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 디텍토리 절대경로와 템플릿 경로를 합침
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
```

## 템플릿 추가하기

1. 밑에 있는 html파일을 템플릿폴더에있는 앱폴더에 추가

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Rango</title>
  </head>
  <body>
    <h1>Rango says...</h1>
    <div>
      hey there partner! <br />
      <strong>{{ boldmessage }}</strong><br />
    </div>
    <div><a href="/rango/about/">About</a><br /></div>
  </body>
</html>
```

<br>

2. `rango/views.py` index 함수에 템플릿을 render()함수를 이용하여 추가한다.

```python
def index(request):
   # context_dict 생성
   context_dict = {'boldmessage' : "Crunchy, creamy, cookie, candy, cupcake!"}

   # client의 요청을 입력받고, rango/index.html 반환
   # html 코드에있는 {{ boldmessage }} 키 값을 받아 밸류를 반환한다.
   return render(request, 'rango/index.html', context=context_dict)
```

<br>

## 스태틱 미디어 디텍토리 구성

### 생성

- 스태틱 미디어 디텍토리는 templates 폴더의 위치에 생성 해야된다.
- e.g ) tango_with_django_project/static
- 이미지 파일을 넣기위해 static 폴더안에 images 폴더를 생성한다.

### 장고에게 경로 추가

- `STATIC_DIR = os.path.join(BASE_DIR, 'static')`
- 위의 명령어를 settings.py에 전에 templates 경로 추가한 밑에줄에 추가한다.
- `STATICFILES_DIRS = [STATIC_DIR, ]` 스태틱파일의 경로가 담긴 경로를 settings.py를 하단에 추가한다.
- `STATIC_URL = '/static/'` 이 [settings.py](http://settings.py) 하단 에 없으면 추가한다.

### 스태틱 미디어 파일과 템플렛

```python
<!DOCTYPE html> # 무조건 첫줄에 넣어야됨 만약 load static다음에 넣으면 html 마크업 유효성검사가 실패하게됨

{% load static %}  # 장고에게 템플릿에있는 스태틱 파일을 쓴다고 알려줌
									 # 그리고 스태틱템플릿을 태그를 사용할 수 있게 해줌 --> '{% %}'

<html>
    <head>
        <title>Rango</title>
    </head>
    <body>
        <h1>Rango says...</h1>
        <div>
            hey there partner! <br/>
            <strong>{{ boldmessage }}</strong><br />
						# 템플릿 태그를 활용하여 static 이미지를 불러옴
            <div>
                <a href="/rango/about">About</a><br />
                <img src="{% static "images/rango.jpg" %}" art="Picture of Rango" />
            </div>
        </div>
    </body>
</html>
```

- 정적 파일을 불러오기 위해 static 명령어를 이용

<br>

### 미디어 파일을 서버상에서 제공하기

- settings.py

```python
# settings.py
# 미디어 경로 설정하기
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

# 빈곳에 루트 설정
MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'     # 마지막에 '/' 잊지말기 콘텐츠를 분리하는 구문

# TEMPLATES 의 context_processors에 media 루트 프로세서 추가하기
'context_processors': [
    'django.template.context_processors.debug',
    'django.template.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.template.context_processors.media'
],
```

- project 디텔토리 [urls.py](http://urls.py) 에서

```python
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns 밑에 static추가
urlpatterns = [

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

## 기본 작업 흐름

# Chapter 5. Models and Databases

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
```

- Database의 테이블을 생성하기 위해 모델을 생성한다.
- 각 클래스는 django.db.models를 상속받아서 사용한다.
- **str**()는 모델의 이름을 정의하기 위한 함수이다. 정의하지 않으면 객체로 이름이 정의되서 나중에 사용하기 번거롭다.

<br>

```python
# 데이터베이스를 생성하기 위한 명령어
# 프로젝트 루트의 manage.py가 있는곳에서 실행해야됨
python manage.py migrate
```
