from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('apps/',apps, name="apps"),
    path('encyrpt/',encyrption,name="encyrption"),
    path('decyrpt/',decyrption,name="decyrption")
]
