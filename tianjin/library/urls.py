from django.urls import path
from . import views

name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/detail/', views.detail, name='detail'),
]