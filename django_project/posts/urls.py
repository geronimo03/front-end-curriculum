from django.urls import path
from posts import views
from .views import PostViewSet
from django.conf.urls import include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', views.PostList),
    path('posts/<int:pk>', views.PostDetail),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]

