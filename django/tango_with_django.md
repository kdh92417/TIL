1. [장고 기본](#-chpater-3-django-basics)

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
