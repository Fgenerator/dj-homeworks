from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    filter = request.GET.get('sort')

    if filter == 'name':
        phones = Phone.objects.order_by('name')
    elif filter == 'min_price':
        phones = Phone.objects.order_by('price')
    elif filter == 'max_price':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.order_by('name')

    context = {
        'phones': phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    phone = Phone.objects.filter(slug=slug).first()

    context = {
        'phone': phone
    }
    return render(request, template, context)
