from django.urls                import path, include
from rest_framework.routers import DefaultRouter
from snippets   import views

from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls))
]

# # bound resource into concrete views
# snippet_list = SnippetViewSet.as_view({
#     'get' : 'list',
#     'post' : 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get' : 'retrieve',
#     'put' : 'update',
#     'patch' : 'partial_update',
#     'delete' : 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get' : 'highlight'
# })
# user_list = UserViewSet({
#     'get' : 'list'
# })
# user_detail = UserViewSet({
#     'get' : 'retrieve'
# })
#
# # register the views with the URL conf as usual
# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('snippets/', snippet_list, name='snippet-list'),
#     path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/', snippet_highlight, name='snippet-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail')
# ])