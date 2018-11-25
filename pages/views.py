# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from master.models import *
from master.views import mysesion
from django.db.models import Q
from .models import Pages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from .forms import *


def recipes_page(request):
    a = Articles.objects.filter(recipe=True, article_publish=True).order_by('-article_date')
    paginator = Paginator(a, 6)
    page = request.GET.get('page')
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)
    return render(request, 'pages/recipes_page.html', {
        'recipes': recipes
        })


def contacts(request):
    if request.POST:
        form = ReCaptchaForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['povaryonok.com@yandex.com'],
                )
            mysesion(request, 'send')
            return redirect('/contacts/')
    else:
        form = ReCaptchaForm()
    return render(request, 'pages/contacts.html', {'form': form})


def sitemap(request):
    return render(request, 'pages/sitemap.html', {
        'pages': Pages.objects.all(),
        'cat': Categories.objects.all()
    })


def aboutsite(request):
    return render(request, 'pages/aboutsite.html', {
        'about': get_object_or_404(Pages, slug=request.path.strip("/"))
    })


def search(request):
    ret_search = request.META.get('HTTP_REFERER', None) or '/'
    if 'q' in request.GET:
        q = request.GET.get('q')
        if not q:
            mysesion(request, "q1")
            return redirect(ret_search + "#ret")
        elif len(q) > 20:
            mysesion(request, "q2")
            return redirect(ret_search + "#ret")
        else:
            articles_search = Articles.objects.filter(Q(article_text__icontains=q))
            return render(request, 'pages/search_results.html', {
                'articles_search': articles_search,
                'q': q
                })
