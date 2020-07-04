"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
##include 추가
from posts.views import main
##views.py에 있는 main 함수로 간다
from lovely.views import first, second, third
##lovely app 안 views.py에 있는 함수들

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main),##, 빼먹지 말기
    path('lovely/', include('lovely.urls')),##이제 lovely/views.py에서 정의해주기
    path('posts/', include('posts.urls')),
]
