from django.urls   import path, include
from .             import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('test/', views.test, name='test'),
    path('recruit/', views.recruit, name='recruit'),
    # path('search/', views.search, name='search'),
]
