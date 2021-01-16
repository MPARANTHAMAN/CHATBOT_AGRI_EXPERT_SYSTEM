from django.urls import path,re_path

from . import views

from caes import views as caes_views




urlpatterns = [
    path('signup',views.signup , name='signup'),
    path('index',views.index , name='index'),
    path('voiceind', views.voiceind, name='voiceind'),
    path('profile', views.profile, name='profile'),
    path('(?P<pk>\d+)/edit/$', views.ProfileView.as_view(), name='edit'),
    
    
    ]