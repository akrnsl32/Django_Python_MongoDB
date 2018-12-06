from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('check_tag', views.check_tag, name="check_tag"),
    path('create_user', views.create_user, name="create_user"),
    path('login',views.login, name="login"),
    path('test',views.getDoc, name="test")
]
