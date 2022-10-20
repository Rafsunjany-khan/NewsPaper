from django.urls import path
from . import views

urlpatterns = [
    path('',views.news, name='home'),
    path('national-news/', views.national, name='national-news'),
    path('international-news/', views.international, name='international-news'),
    path('entertainment-news/', views.entertainment, name='entertainment-news'),
    path('play-news/', views.play, name='play-news'),
    path('contract/', views.contract, name='contract'),
    path('news-details/<pk>', views.news_details, name='news-details'),
]