from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')

    if sort == 'name':
        order_by = 'name'
    elif sort == 'min_price':
        order_by = 'price'
    elif sort == 'max_price':
        order_by = '-price'
    else:
        return HttpResponse(status=400)

    catalog_phone = list(Phone.objects.order_by(order_by).all())
    context = {
        'phones': catalog_phone
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    try:
        phone = Phone.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    context = {
        'phone': phone
    }
    return render(request, template, context)
