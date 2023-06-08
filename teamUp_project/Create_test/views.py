from django.http import HttpResponse
from django.shortcuts import render


def head_page(request):
    return HttpResponse('Главная страница')


def create_test(request):
    return HttpResponse('<h1>Создание теста</h1>')
