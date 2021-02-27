3. [Chaper 3. Django Basics](#-chpater-3-django-basics)

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
