from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('mp3/', views.convert_url_to_mp3, name='url-mp3'),
    path('mp4/', views.convert_url_to_mp4, name='url-mp4'),
    path('wav/', views.convert_url_to_wav, name='url-wav'),
    path('webm/', views.convert_url_to_webm, name='url-webm'),
    path('mov/', views.convert_url_to_mov, name='url-mov'),
]
