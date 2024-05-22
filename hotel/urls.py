from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact,name='contact'),
    path('about/', views.about, name='about'),
    path('reservation/<int:room_id>/', views.ReservationView.as_view(), name='reservation'),
    path('reservation_confirmation/<int:reservation_id>/', views.reservation_confirmation, name='reservation_confirmation'),
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/add/', views.add_room, name='add_room'),
    path('rooms/edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('rooms/delete/<int:room_id>/', views.delete_room, name='delete_room'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('logout_success/', views.logout_success, name='logout_success'),
    path('signup/', views.signup, name='signup'),
    
]