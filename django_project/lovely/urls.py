from django.urls import path
from .views import first, second, third, new, create, view, edit, update, delete

app_name='lovely'##한 번에 묶기
urlpatterns=[
    path('first/', first, name="first"),
    path('second/', second, name="second"),
    path('third/', third, name="third"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('<int:post_id>/', view, name="view"),
    path('edit/<int:post_id>/', edit, name="edit"),
    path('update/<int:post_id>/', update, name="update"),
    path('delete/<int:post_id>/', delete, name="delete"),
]
