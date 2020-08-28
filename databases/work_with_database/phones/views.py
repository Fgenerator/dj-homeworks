from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    sort_dict = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }

    phones = Phone.objects.all()
    sort_key = request.GET.get('sort')

    if sort_key:
        phones = phones.order_by(sort_dict.get(sort_key))
    return render(
        request,
        'catalog.html',
        context={'phones': phones}
    )


def show_product(request, slug):
    template = 'product.html'

    phone = Phone.objects.filter(slug=slug).first()

    context = {
        'phone': phone
    }
    return render(request, template, context)
