from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp_form, name='emp_form'),
    path('check_emp_code/', views.check_emp_code, name='check_emp_code'),
    path('check_location/', views.check_location, name='check_location'),
]