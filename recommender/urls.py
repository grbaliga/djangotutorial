from django.urls import path
from . import views

app_name = 'recommender'

urlpatterns = [
    path('best/', views.searchform, name='best'),
]
 