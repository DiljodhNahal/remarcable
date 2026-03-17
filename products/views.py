from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from .models import Product
from .forms import ProductFilterForm


def product_list(request) -> HttpResponse:
    """
    Display a list of products with optional search and filtering.
    """

    form = ProductFilterForm(request.GET or None)
    products = Product.objects.select_related('category').prefetch_related('tags')

    if form.is_valid():
        search = form.cleaned_data.get('search')
        category = form.cleaned_data.get('category')
        tags = form.cleaned_data.get('tags')

        if search:
            products = products.filter(description__icontains=search)

        if category:
            products = products.filter(category=category)

        if tags:
            for tag in tags:
                products = products.filter(tags=tag)

    products = products.distinct()

    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    query_params = request.GET.copy()
    query_params.pop('page', None)

    context = {
        'form': form,
        'products': page_obj,
        'result_count': paginator.count,
        'query_string': query_params.urlencode(),
    }

    return render(request, 'products/product_list.html', context)
