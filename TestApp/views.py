from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from TestApp.forms import SignUpForm
from django.http import HttpResponseRedirect


def home_page_view(request):
    return render(request,'testApp/home.html',)

@login_required
def java_exam(request):
	return render(request,'testApp/java.html')

@login_required
def python_exam(request):
    return render(request,'testApp/python.html')
    
@login_required
def aptitude_exam(request):
    return render(request,'testApp/aptitude.html')


def logout_view(request):
    return render(request,'testApp/logout.html')

def sign_up_view(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testApp/signup.html',{'form':form})





