from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('posts/', PostList.as_view(), name='posts'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='detail'),
    path('authors/', AuthorList.as_view(), name='authors'),
    path('categories/', CategoryList.as_view(), name='categories'),
    path('tags/', TagList.as_view(), name='tags'),
    path('subscribe/', SubscribeList.as_view(), name='subscribe')
]