from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.
@login_required
@permission_required('global_permissions.home_home', login_url='nopermissions')
def home(request):
    return render(request, 'home.html')


def index(request):
    return render(request, 'index.html')



def nopermissions(request):
    return render(request, 'no-permission.html')
