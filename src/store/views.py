from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from store.forms import CategoryForm, ProductForm, AddForm
from store.models import Category, Product, ProductIn


def home(request):
    return render(request, 'index.html')


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'store/category_add.html'
    success_url = reverse_lazy('store:create_category')


def create_product(request):
    form = ProductForm
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'store/product_create.html', {'form': form})
    else:
        return render(request, 'store/product_create.html', {'form': form})


def products(request):
    objects = Product.objects.all()
    paginator = Paginator(objects, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}

    return render(request, 'store/products.html', context)


def product_add(request, pk=None):
    form = AddForm
    if pk:
        if request.method == 'POST':
            form = AddForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                product = Product.objects.get(pk=pk)
                product.count += data['count']
                product.save()
                return redirect('store:products')
        qs = get_object_or_404(Product, id=pk)
        return render(request, 'store/product_add.html', {'object': qs, 'form': form})

    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product = data['product']
            product = Product.objects.get(pk=product.pk)
            product_in = ProductIn()
            product_in.product = product
            product_in.count = data['count']
            product_in.price = product.price
            product_in.save()
            product.count += data['count']
            product.save()
            return redirect('store:products')

    return render(request, 'store/product_add.html', {'form': form})


def detail(request, pk=None):
    if pk:
        qs = get_object_or_404(Product, id=pk)
        context = {'object': qs}
        return render(request, 'store/detail.html', context)
    return render(request, 'store/detail.html')
