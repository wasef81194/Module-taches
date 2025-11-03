from django.urls import path
from .views import home,new,delete

urlpatterns = [
    path('', home, name='home'),
    path('taches/new', new, name='new'),
    path('tache/delete', delete, name='delete'),
]