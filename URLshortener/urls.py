from django.contrib import admin
from django.urls import path
from urls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main_page'),
    path('add_url/', views.add_url, name='add_url'),
]