
from django.urls import path
from irabbit.contas.views import list, cadastro, atualizar, apagar


urlpatterns = [
    path('', list, name='list'),
    path('novo', cadastro, name='cadastro'),
    path('update/<int:id>/', atualizar, name='atualizar'),
    path('atualizar/<int:id>/', atualizar, name='atualizar'),
    path('apagar/<int:id>/', apagar, name='apagar')

]
