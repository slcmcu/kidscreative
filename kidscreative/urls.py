"""kidscreative URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
from kidscreative.settings import MEDIA_ROOT

import xadmin

from blog.views import ArticlesListView, ArticleDetailView, LabelSearchView
from main.views import IndexPageView, ContactView
from courses.views import CoursesListView, CourseDetailView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^blog/$', ArticlesListView.as_view(), name='blog'),
    url(r'^blog/article_(?P<id>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
    url(r'^blog/label_(?P<label>\w+)/$', LabelSearchView.as_view(), name='label_search'),

    url(r'^$', IndexPageView.as_view(), name='index'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),

    url(r'^course/$', CoursesListView.as_view(), name='course'),
    url(r'^course/detail_(?P<id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),

]
