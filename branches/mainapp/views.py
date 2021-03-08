from django.shortcuts import render, HttpResponseRedirect
from .forms import EmployeeForm, BranchForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='/in/login')
def create(request):
    error = ''
    if request.method == 'POST':
        if 'branch' in request.POST:
            branchform = BranchForm(request.POST, request.FILES)
            if branchform.is_valid():
                branchform.save()
                return HttpResponseRedirect("/")
            else:
                error = 'Incorrect validation'
        elif 'employee' in request.POST:
            employeeform = EmployeeForm(request.POST)
            if employeeform.is_valid():
                employeeform.save()
                return HttpResponseRedirect('/')
            else:
                error = 'Incorrect validation'
    employeeform = EmployeeForm()
    branchform = BranchForm()
    data = {
        'form1': employeeform,
        'form2': branchform,
        'error': error
    }
    return render(request, 'mainapp/map.html', data)