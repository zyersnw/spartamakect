from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('<int:item_id>/', views.item_detail, name='item_detail'),
    path('create/', views.item_create, name='item_create'),
    path('<int:item_id>/update/', views.item_update, name='item_update'),
    path('<int:item_id>/delete/', views.item_delete, name='item_delete'),
    path('<int:item_id>/like/', views.like_item, name='like_item'),
    path('<int:item_id>/favorite/', views.favorite_item, name='favorite_item'),
    path('<int:item_id>/comment/', views.add_comment_to_item, name='add_comment_to_item'),
]
