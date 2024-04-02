from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegisterView.as_view(), name='registration'),
    path('authorization/', views.LoginView.as_view(), name='authorization'),
    path('confirm/', views.ConfirmAPIView.as_view(), name='confirm_api_view'),
]
