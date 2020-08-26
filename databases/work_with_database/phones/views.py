from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    phones = Phone.objects.all()

    context = {
        'players': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
