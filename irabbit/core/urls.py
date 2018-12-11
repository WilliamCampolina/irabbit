from django.urls import path, include
from irabbit.core.views import home, index, nopermissions


urlpatterns = [
    path('', index, name='index'),
    path('home', home, name='home'),
    path('nopermissions', nopermissions, name='nopermissions')

]
