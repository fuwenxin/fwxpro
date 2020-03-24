from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegForm
from django.contrib.auth.models import User

def User_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            login(request,user)
            return redirect('user_detail')
    login_form = LoginForm()
    context = {'login_form':login_form,}
    return render(request,'login.html',context)

def User_register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            user = User.objects.create_user(username,email,password)
            user.save()
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('user_detail')
    reg_form = RegForm()
    context = {'reg_form': reg_form, }
    return render(request, 'register.html', context)

def User_logout(request):
    logout(request)
    return redirect('login')