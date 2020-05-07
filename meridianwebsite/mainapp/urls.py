from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.services, name='services'),
    path('dialysis', views.dialysis, name='dialysis'),
    path('dental', views.dental, name='dental'),
    path('physiotherapy', views.physiotherapy, name='physiotherapy'),
    path('diagnostic', views.diagnostic, name='diagnostic'),
]