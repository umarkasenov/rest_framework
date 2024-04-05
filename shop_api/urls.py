from django.urls import path, include
from django.contrib import admin
from . import yasg


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('api/v1/product/', include('product.urls')),
    path('api/v1/users/', include('users.urls')),
]

urlpatterns += yasg.urlpatterns
