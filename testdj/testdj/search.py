# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response, render


def search_form(request):
    return render_to_response('search_form.html')


def search_result(request):
    request.encoding = 'utf-8'
    print request.GET['q']
    if not request.GET['q'] == '':
        message = {
            'message': 'The content of your searching is %s.' % (request.GET['q'])
        }
    else:
        message = {'message': 'You input the empty table.'}
    return render(request, 'search_result.html', message)
