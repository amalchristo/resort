from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('',views.index,name='index'),
    path('profile',views.profile,name='profile'),
    path('logout',views.logout,name='logout')

]