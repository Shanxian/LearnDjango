# -*- coding: utf-8 -*-
# from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context = {
        'hello': 'Hello Sports!',
        'sportList': [
            {
                'name': 'Patter',
                'age': 24,
                'height': 177
            },
            {
                'name': 'Mark',
                'age': 23,
                'height': 180
            },
            {
                'name': 'Mark',
                'age': 17,
                'height': 165
            }
        ]
    }
    return render(request, 'hello.html', context)
