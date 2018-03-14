from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# 실제로 어떤 기능을 만들어 내는 부분
# 글을 쓸 때, 수정할 때, 지울 때, 볼 때 어떻게 해당 기능이 동작할 것인지
# Create your views here.

from .models import Bookmark
from django.urls import reverse_lazy

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    # bookmark_form.html
    # template_name = 'aaa.html'
    template_name_suffix = '_create'
    # bookmark_create.html

    model = Bookmark

    # 입력받을 필드 목록
    fields = ['site_name', 'url']

    # 글쓰기가 완료된 후에 이동할 페이지
    # reverse
    # url 패턴 -> url
    # url
    # lazy
    # lazy가 없으면 바로 url이 만들어져 있는 형태
    # lazy가 있으면 실행할 때 url을 만들어서 던져줍니다.

    success_url = reverse_lazy('bookmark:index')

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'
    success_url = reverse_lazy('bookmark:index')

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')

class BookmarkDetailView(DetailView):
    model = Bookmark