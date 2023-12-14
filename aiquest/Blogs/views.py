from django.http import HttpResponse
from django.shortcuts import render
from Blogs.models import Teacher
from . forms import TeachersRegistration
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def blogs(request):
    #print(request)
    return render(request,'blogs/blogs.html') 
    #HttpResponse('Welcome to Django  Blogs:   <br>1. http://127.0.0.1:8000/blog/')


def teachers_info(request):
    teach = Teacher.objects.all()
    return render(request,'blogs/t.html', {'thr':teach})

def showFormsData(request):

    if request.method == 'POST':
        fm=TeachersRegistration(request.POST)
        #print(fm)
        if fm.is_valid():
            #print('This is POST Statement') 
            print(fm.cleaned_data['password'])
            print(fm.cleaned_data['repassword'])
    else:
        fm=TeachersRegistration()
        print('This is GET Statement')
    #fm.order_fields(field_order=['email'])
    return render(request,'blogs/forms.html',{'form': fm})

def registration(request):

    if request.method=='POST':
        rg=UserCreationForm(request.POST)
        if rg.is_valid():
            rg.save()
    else:
        rg = UserCreationForm()
    return render(request,'blogs/register.html',{'reg': rg})
