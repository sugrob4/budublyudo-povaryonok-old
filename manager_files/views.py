# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from manager_files.models import Upload
from django.http import HttpResponse


@login_required
def image_browser(request):
    data = Upload.objects.order_by('-add_date')
    callback = request.GET.get('CKEditorFuncNum', None)
    return render_to_response('manager/browse.html', {
        'data': data, 'callback': callback
    })


@login_required
@csrf_exempt
def image_uploader(request):
    forw = request.META['HTTP_REFERER']
    try:
        file = request.FILES['upload']
        upload = Upload(image=file)
        upload.save()
    except Exception:
        html = '<p>Ошибка при загрузке файла&nbsp;<a href="%s">Вернуться назад</a></p>' % forw
        return HttpResponse(html)
    return redirect(forw)
