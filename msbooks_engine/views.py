import datetime

from django.shortcuts import render


def index(request):
    date = datetime.datetime.now().date()
    context = {
        'date': date
    }
    return render(request, 'msbooks_engine/index.html', context)
