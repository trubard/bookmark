from django.urls import path, re_path
from .views import *

# 어떤 주소로 접속했을 때, 어떤 기능(뷰)를 동작시킬 것인지 매칭 시키는 부분
# 1차 라우팅, 2차 라우팅
# 1차 라우팅 : 프로젝트 메인 urls.py
# 2차 라우팅 : 각 앱의 urls.py

# path : 어떤 주소로 접속했을 때 어떤 뷰를 동작시킬 것이냐
# re_path : 어떤 주소(정규표현식)로 접속했을 때 어떤 뷰를 동작시킬 것이냐
app_name = 'bookmark'

urlpatterns = [
    path('', BookmarkListView.as_view(), name='index'),
    path('add/', BookmarkCreateView.as_view(), name='create'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
    path('view/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    # bookmark:create -> bookmark/add/
    # bookmark:update -> bokkmark/update/?
]
