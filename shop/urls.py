from django.urls import path, include
from . import views
from .views import all_skills, skill_detail

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('author/', views.author, name='author'),
    path('spec/', all_skills),
    path('spec/<int:id>/', skill_detail), 
]