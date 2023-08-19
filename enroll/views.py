from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.




#This Function we used to add new item and show that item
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,enroll=em,password=pw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud}) 


#This  function update and edit
def update_data(request):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        else:
            pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=pi)
    return render(request,'enroll/updatestudent.html',{'form':fm})


#This function for delete data

def delete_data(request):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')