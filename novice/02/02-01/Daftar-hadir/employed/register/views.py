from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import form
from . models import register

# Create your views here.
def employed_list(request):
    context = {'employed_list':register.objects.all()}
    return render(request,"registrasi/employed_list.html",context)

def employed_form(request):
    form_input = form.EmployedForm()
    if request.POST:
        form_input= form.EmployedForm()
        if form_input.is_valid():
            form_input.save()
        return redirect('/employed/list/')  
    return render(request,"registrasi/employed_form.html",{
        'form':form_input
        })
# def employed_delete(request):
#     return