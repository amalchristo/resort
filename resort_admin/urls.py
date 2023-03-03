from django.urls import path
from . import views
app_name = 'resort_admin'

urlpatterns = [
    path('admin_master',views.admin_master,name='admin_master'),
    path('add_room',views.add_room,name='add_room'),
    path('staff_details',views.staff_details,name='staff_details'),
    path('add_staff',views.add_staff,name='add_staff'),
    path('room_details',views.room_details,name='room_details'),
    path('',views.admin_login,name='admin_login'),
    path('delete_room/<int:room_id>',views.delete_room,name='delete_room'),
    path('room_book',views.room_book,name='room_book'),
    # path('delete_book',views.delete_book,name='delete_book')
    ]