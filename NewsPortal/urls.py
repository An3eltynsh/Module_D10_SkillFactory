from django.urls import path
from .views import (
    NewsList, NewDetail, NewsSearch, CreateNews,
    CreatePost, NewsUpdate, PostUpdate, NewsDelete,
    IndexView, PostDelete, BaseRegisterView,
    become_author,
    CategoryNewsList,
    subscribe,
    unsubscribe
)
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('', NewsList.as_view(), name='list'),
    path('<int:pk>', NewDetail.as_view(), name='new'),
    path('search/', NewsSearch.as_view()),
    path('create/', CreateNews.as_view(), name='news_create'),
    path('post/create/', CreatePost.as_view(), name='post_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('post/<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('post/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('userprofil/', IndexView.as_view(), name = 'userprofil'),
    path('login/',  LoginView.as_view(template_name='sign/login.html'), name='login'), #template_name='sign/login.html'
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', BaseRegisterView.as_view(template_name='sign/signup.html'), name='signup'),
    path('authors/', become_author, name = 'authors'),
    path('categories/<int:pk>', CategoryNewsList.as_view(), name = 'categories'),
    path('categories/<int:pk>/subscribe', subscribe, name = 'subscribe'),
    path('categories/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe')
    ]
