from django.http import HttpResponse

from .models import Bd

def index(request):
    s = 'Список объявлений\r\n\r\n\r\n'
    for bd in Bd.objects.order_by('-published'):
        s += bd.title + '\r\n' + bd.content + '\r\n\r\n'
    return HttpResponse(s, content_type='text/plain; charset=utf-8')
# Create your views here.
