
from django.urls import path
from irabbit.produto.views import index, cadastro, atualizar, apagar


urlpatterns = [
    path('', index, name='produto.index'),
    path('novo', cadastro, name='produto.cadastro'),
    path('atualizar/<int:id>/', atualizar, name='produto.atualizar'),
    path('apagar/<int:id>/', apagar, name='produto.apagar'),
]
