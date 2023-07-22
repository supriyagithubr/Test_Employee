from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee


# Create your views here.

def addEmployeeView(request):
    form = EmployeeForm()
    template_name = "app1/add.html"
    context = {'form':form}
    if request.method == 'POST':
        form= EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,template_name,context)


def showEmployeeView(request):
    data = Employee.objects.all()
    template_name = 'app1/show.html'
    context = {'obj': data}
    return render(request,template_name,context)



def updateEmployeeView(request, pk):
    ord = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=ord)
    template_name = 'app1/add.html'
    context = {'form': form}
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=ord)
        if form.is_valid():
            form.save()
            return redirect('showemployee_url')
    return render(request,template_name,context)


def deleteEmployeeView(request, pk):
    ord = Employee.objects.get(id=pk)
    template_name = 'app1/confirm.html'
    context = {'data':ord}
    if request.method == 'POST':
        ord.delete()
        return redirect('showemployee_url')
    return render(request,template_name,context)