
from django.urls import path
from irabbit.item.views import index, atualizar, cadastro, apagar



urlpatterns = [

    path('', index, name='item.index'),
    path('novo', cadastro, name='item.cadastro'),
    path('atualizar/<int:id>/', atualizar, name='item.atualizar'),
    path('apagar/<int:id>/', apagar, name='item.apagar')

]
