from posts.views import PostViewSet, UserViewSet, api_root
from django.conf.urls import include
from rest_framework import routers, renderers
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts import views


router = DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]


snippet_list = PostViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
snippet_highlight = PostViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})