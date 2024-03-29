from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.register, name='registration'),
    path('authorization/', views.authorization, name='authorization'),
    path('confirm/', views.confirm_api_view, name='confirm_api_view'),
]
