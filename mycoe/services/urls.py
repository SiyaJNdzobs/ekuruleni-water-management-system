from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report, name='report'),
    path('pay/', views.pay, name='pay'),
    path('status/', views.status, name='status'),
]