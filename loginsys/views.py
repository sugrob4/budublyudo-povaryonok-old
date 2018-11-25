# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from loginsys.forms import RegistrationForm
from django.template.context_processors import csrf


def login_user(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse('ok', content_type='text/html')
        else:
            return HttpResponse('Неверный логин или пароль!', content_type='text/html')
    else:
        return HttpResponse('Ошибка авторизации!', content_type='text/html')


def logout_user(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'] + "#ret")


def register(request):
    args = {}
    args.update(csrf(request))
    args['form'] = RegistrationForm()
    if request.POST:
        newuser_form = RegistrationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = authenticate(
                username=newuser_form.cleaned_data['username'],
                email=newuser_form.cleaned_data['email'],
                password=newuser_form.cleaned_data['password2']
            )
            login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
            args['reg'] = 'reg'
    return render(request, 'content/registration.html', args)
