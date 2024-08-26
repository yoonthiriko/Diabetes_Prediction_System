from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path("predict/", views.predict, name='predict'),
    path("predict/result", views.result, name='result'),
]
