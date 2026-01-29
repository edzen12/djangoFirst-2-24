from django.urls import path 
from apps.about.views import about, employee


urlpatterns = [ 
    path('', about, name='about'),
    path('employee/', employee, name='employee'),
]