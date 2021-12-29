from django.urls   import path
from .             import views
from .views import SearchView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('test/', views.test, name='test'),
    path('recruit/', views.recruit, name='recruit'),
    path('search', SearchView.as_view(), name='search'),
]
