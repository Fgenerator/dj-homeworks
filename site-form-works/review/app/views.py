from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views import View

from .models import Product, Review
from .forms import ReviewForm


def product_list_view(request):
    template = 'app/product_list.html'
    products = Product.objects.all()

    context = {
        'product_list': products,
    }

    return render(request, template, context)


def product_view(request, pk):
    template = 'app/product_detail.html'
    product = get_object_or_404(Product, id=pk)
    reviews = Review.objects.filter(product=product)
    is_review_exist = False

    request.session.get('reviewed_products', [])
    if pk in request.session['reviewed_products']:
        is_review_exist = True

    form = ReviewForm
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if pk not in request.session['reviewed_products']:
                Review.objects.create(**form.cleaned_data, product=Product.objects.get(id=pk))
                is_review_exist = True
                reviewed_products_list = request.session.get('reviewed_products', [])
                reviewed_products_list.append(pk)
                request.session['reviewed_products'] = reviewed_products_list
        # логика для добавления отзыва

    context = {
        'form': form,
        'product': product,
        'reviews': reviews,
        'is_review_exist': is_review_exist
    }

    return render(request, template, context)


class ProductView(View):  # вариант решения через class based view
    template = 'app/product_detail.html'
    is_review_exist = False
    form = ReviewForm

    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        reviews = Review.objects.filter(product=product)

        reviewed_products_list = request.session.get('reviewed_products', [])

        if pk in reviewed_products_list:
            self.is_review_exist = True

        context = {
            'form': self.form,
            'product': product,
            'reviews': reviews,
            'is_review_exist': self.is_review_exist
        }

        return render(request, self.template, context)

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        reviews = Review.objects.filter(product=product)

        reviewed_products_list = request.session.get('reviewed_products', [])

        if pk in reviewed_products_list:
            self.is_review_exist = True

        self.form = ReviewForm(request.POST)
        if self.form.is_valid():
            if pk not in reviewed_products_list:
                Review.objects.create(**self.form.cleaned_data, product=Product.objects.get(id=pk))
                self.is_review_exist = True
                reviewed_products_list.append(pk)
                request.session['reviewed_products'] = reviewed_products_list
        # логика для добавления отзыва

        context = {
            'form': self.form,
            'product': product,
            'reviews': reviews,
            'is_review_exist': self.is_review_exist
        }

        return render(request, self.template, context)
