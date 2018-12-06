from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('db_insert', views.db_insert, name='db_insert)'),
    path('db_get', views.db_get, name='db_get'),
    path('create_user', views.create_user, name='create_user'),
    path('request_post', views.request_post, name='request_post'),
    path('request_get',views.request_get, name='request_get')
]
