"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, re_path, include
from bookmark.views import BookmarkListView

# 어떤 주소로 접속했을 때, 어떤 기능(뷰)를 동작시킬 것인지 매칭 시키는 부분
# 1차 라우팅, 2차 라우팅
# 1차 라우팅 : 프로젝트 메인 urls.py
# 2차 라우팅 : 각 앱의 urls.py

# path : 어떤 주소로 접속했을 때 어떤 뷰를 동작시킬 것이냐
# re_path : 어떤 주소(정규표현식)로 접속했을 때 어떤 뷰를 동작시킬 것이냐
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookmark/', include('bookmark.urls', namespace='bookmark')),
    path('', BookmarkListView.as_view(), name='index')
]
