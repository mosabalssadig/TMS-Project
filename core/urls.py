from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index, name="index",),
    path("addUser", views.addUser, name="addUser",),
    path("attendance", views.attendance, name="attendance",),
    path("addTask", views.addTask, name="addTask",), 
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('deleteuser', views.deleteuser, name='deleteuser'),
]
