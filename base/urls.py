from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_page, name="app_login"),
    path('register/', views.register_page, name="app_register"),
    path('logout/', views.logout_user, name="app_logout"),
    path('profile/<str:pk>', views.user_profile, name="app_user_profile"),

    path('', views.home, name='home'),
    path('room/<str:pk>/', views.room, name='room'),

    path('create-room/', views.create_room, name="app_create_room"),
    path('update-room/<str:pk>/', views.update_room, name="app_update_room"),
    path('delete-room/<str:pk>/', views.delete_room, name="app_delete_room"),
    path('delete-message/<str:pk>/',
         views.delete_message, name="app_delete_message"),

    path('update-user/', views.update_user, name="app_update_user"),
    path('topics/', views.topics_page, name="app_topics"),
    path('activity/', views.activity_page, name="app_activity"),

]
