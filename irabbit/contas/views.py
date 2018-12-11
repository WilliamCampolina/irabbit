from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

from irabbit.contas.models import TipoConta, Conta
from irabbit.contas.forms import ContaForm




@login_required
@permission_required('contas.view_conta', login_url='nopermissions')
def list(request):
    tipoContas = TipoConta.objects.all()
    contas = Conta.objects.all()

    return render(request, 'contas/list.html', {'contas': contas, 'tipoContas': tipoContas})

@login_required
@permission_required('contas.add_conta', login_url='nopermissions')
def cadastro(request):
    form = ContaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'contas/cadastro.html', {'form': form})

@login_required
@permission_required('contas.change_conta', login_url='nopermissions')
def atualizar(request, id):
    conta = Conta.objects.get(id=id)
    form = ContaForm(request.POST or None, instance=conta)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'contas/cadastro.html', {'form': form, 'conta': conta})

@login_required
@permission_required('contas.delete_conta', login_url='nopermissions')
def apagar(request, id):
    conta = Conta.objects.get(id=id)

    if request.method == 'POST':
        conta.delete()
        return redirect(list)

    return render(request, 'contas/delete.html', {'conta': conta})
