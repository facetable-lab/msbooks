from django.shortcuts import render

from .forms import SubscriberForm


def index(request):
    form = SubscriberForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        form.save()

    context = {
        'form': form
    }

    return render(request, 'msbooks_engine/index.html', context)
