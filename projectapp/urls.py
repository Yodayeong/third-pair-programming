from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('',views.index, name='index'),
    path('new/',views.new, name='new'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('delete/<int:pk>',views.delete, name='delete'),
    path('update/<int:pk>',views.update, name='update'),
    path('updateF/<int:pk>',views.updateF, name='updateF')
]