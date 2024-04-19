from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login, name='login'),
    path('user_logout/', views.user_logout, name='logout'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('<int:item_id>/', views.item_detail, name='item_detail'),
]
