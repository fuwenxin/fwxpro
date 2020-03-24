from django.urls import path
from . import views

urlpatterns = [
    path('',views.User_detail,name='user_detail'),
    path('user_info/',views.User_info,name="user_info"),
    path('data_list/<int:list_pk>',views.Data_list,name='data_list'),
]