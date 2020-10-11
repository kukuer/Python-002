from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .form import LoginForm


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_info = login_form.cleaned_data
            user = authenticate(username=user_info['username'], password=user_info['password'])
        if user:
            login(request, user)
            return render(request, 'index.html')
        else:
            return HttpResponse('登录失败：密码错误')
        

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request, 'login.html', {'form': login_form})

