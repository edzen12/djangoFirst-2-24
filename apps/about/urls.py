from django.urls import path 
from apps.about.views import about, employee, employee_detail


urlpatterns = [ 
    path('', about, name='about'),
    path('employee/', employee, name='employee'),
    path('employee/<slug:slug>/', employee_detail, name='employee_detail'),
]