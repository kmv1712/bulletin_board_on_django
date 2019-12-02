from django.shortcuts import render

from .models import Bd

def index(request):
    bbs = Bd.objects.order_by('-published')
    return render(request, 'bboard/index.html', {'bbs': bbs})
# Create your views here.
