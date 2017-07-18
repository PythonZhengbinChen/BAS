"""bas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib import admin
import django.views.static

from bas import settings
from blog import views
from blog.control import bookControl
from blog.control import searchControl


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^author/$', views.author, name='author'),
    url(r'^book_info/$', views.book_info, name='book_info'),
    url(r'^publish_info/$', views.publish_info, name='publish_info'),
    url(r'^getTopTenBook/$', bookControl.getTopTenBookInfo, name='getTopTenBook'),
    url(r'^getTopTenAuthor/$', bookControl.getTopTenAuthor, name='getTopTenAuthor'),
    url(r'^getTopTenPublishing/$', bookControl.getTopTenPublishing, name='getTopTenPublishing'),
    url(r'^searchRequest/$', searchControl.setSearchToHTML, name='searchRequest'),
    url(r'^getBookMainInfo/$', searchControl.getBookMainInfo, name='getBookMainInfo'),
    url(r'^getRelevanceBook/$', searchControl.getRelevanceBook, name='getRelevanceBook'),
    url(r'^getAuthorInfo/$', searchControl.getAuthorInfo, name='getAuthorInfo'),
    url(r'^getAuthorPublishList/$', searchControl.getAuthorPublishList, name='getAuthorPublishList'),
]
