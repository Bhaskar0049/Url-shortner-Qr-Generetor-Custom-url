from django.contrib import admin
from django.urls import path,include
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.index, name='index'),
    path('site/shorturl/', views.shorturl, name='shorturl'),
    path('<str:short_url>/', views.redirect_original, name='redirect_original'),
    path('qr/qrcode/', views.generate_qr, name='qrcode'),
    path('site/custom_url/', views.customurl, name='customurl'),
    path('c/<str:customurl>/', views.redirect_custom_to_original, name='custom_original'),
    path('site/about/', views.about, name='about'),
    path('site/policy/', views.privacy, name='policy'),
]

