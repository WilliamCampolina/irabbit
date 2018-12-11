from django.urls import path
from irabbit.pedido.views import index



urlpatterns = [
    path('', index, name='pedido.index'),
    # path('novo', cadastro, name='cadastro'),
    # path('update/<int:id>/', atualizar, name='atualizar'),
    # path('atualizar/<int:id>/', atualizar, name='atualizar'),
    # path('apagar/<int:id>/', apagar, name='apagar')

]