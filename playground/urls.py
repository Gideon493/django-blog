from unicodedata import name
from django.urls import URLPattern, path
from . import views

#app_name = 'playground'


urlpatterns = [
    path('', views.hello, name='home'),
    path('members/', views.members_list, name='members'),
    path('members/<str:firstname>/', views.members_detail, name='member'),
    path('blog/', views.create_blog_view, name='blog'),
    path('articles/', views.blog_article_view, name='articles'),
    path('articles/<str:title>/', views.article_detail_view, name='article')

]
