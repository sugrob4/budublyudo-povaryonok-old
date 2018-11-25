# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404, render_to_response
from django.http import Http404
from .models import *
from master.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def mysesion(request, var):
    request.session[var] = True
    request.session.set_expiry(1)


def home(request):
    articles = Articles.objects.filter(article_publish=True)
    return render(request, 'content/popular_newrecipes.html', {
        'home_popular': articles.order_by('?')[:5],
        'recipe': articles.filter(recipe=True).order_by('-article_date')[:5],
    })


def categories(request, pk):
    p = Articles.objects.filter(category_article_id=pk)
    paginator = Paginator(p, 6)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    return render(request, 'content/categories.html', {
        'articles': articles,
        'cat_krohi': get_object_or_404(Categories, category_id=int(pk))
    })


def view_detailed(request, pk):
    try:
        article_detail = get_object_or_404(Articles, pk=int(pk))
    except Articles.DoesNotExist:
        raise Http404('404.html')
    return render(request, 'content/view_detailed.html', {
        'article_detail': article_detail,
        'cat': get_object_or_404(Categories, pk=article_detail.category_article_id)
    })


def addcomment(request, pk):
    if request.POST:
        if "but" not in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.comments_article = Articles.objects.get(pk=int(pk))
                form.save()
        else:
            mysesion(request, "e")
            redirect('/article/%s' % pk + "#comment")
    return redirect('/article/%s' % pk + "#comment")


def registration(request):
    return render(request, 'content/registration.html',)


def robots(request):
    return render_to_response('robots.txt', content_type="text/plain")

def dublin(request):
    return render_to_response('dublin.rdf', content_type="application/rdf+xml")

