from django.urls import path
from irabbit.pedido.views import index, cadastro, atualizar,apagar



urlpatterns = [
    path('', index, name='pedido.index'),
    path('novo', cadastro, name='pedido.cadastro'),
    path('atualizar/<int:id>/', atualizar, name='pedido.atualizar'),
    path('apagar/<int:id>/', apagar, name='pedido.apagar')

]