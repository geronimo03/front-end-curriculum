from django.urls import path
from .views import new, create, show, edit, update, delete, PostViewSet
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('post', PostViewSet)

app_name = "posts"
urlpatterns = [
    path('', include(router.urls)),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:post_id>/', show, name="show"),
    path('edit/<int:post_id>/', edit, name="edit"),
    path('update/<int:post_id>/', update, name="update"),
    path('delete/<int:post_id>/', delete, name="delete"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
