
from django.urls import path
from irabbit.usuarios.views import db_login, register, db_logout
#from despesas.contas.views import list, cadastro, atualizar, apagar


urlpatterns = [
    path('login', db_login, name='login'),
    path('logout', db_logout, name='logout'),
    path('register', register, name='register')
    # path('novo', cadastro, name='cadastro'),
    # path('update/<int:id>/', atualizar, name='atualizar'),
    # path('atualizar/<int:id>/', atualizar, name='atualizar'),
    # path('apagar/<int:id>/', apagar, name='apagar')

]
