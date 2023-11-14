from django.shortcuts import render
from django.http import HttpResponse
from bboard.models import Bb
from django.template import loader
import requests


def index(request):
    response = requests.get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()
    output = ""
    for item in data:
        output += f"ID: {item['id']}, Заголовок: {item['title']}, Статус: {'Завершено' if item['completed'] else 'Не завершено'}\r\n\r\n"
    return render(request, 'index.html', {'output': output})


def index_old(request):
    template = loader.get_template('index.html')
    bbs = Bb.objects.order_by('-published')
    context = {'bbs': bbs}
    return HttpResponse(template.render(context, request))