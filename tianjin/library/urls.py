from django.urls import path
from . import views

app_name = 'library'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/detail/', views.detail, name='detail'),
    path('liste/', views.liste, name='liste'),
    path('resultat/', views.resultat, name='resultat'),
    path('list_by_category/', views.list_by_category, name='list_by_category')
]