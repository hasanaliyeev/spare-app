from django import forms

from store.models import Category, Product


class CategoryForm(forms.ModelForm):
    name = forms.CharField(label='Name',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Category name'}))
    parent = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    slug = forms.CharField(label='Slug',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug name'}))

    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Product name'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    price = forms.DecimalField(label='Price', widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Price'
    }))
    count = forms.IntegerField(label='Count', widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Count'
    }))
    description = forms.CharField(label='Description', required=False, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Description'
    }))

    class Meta:
        model = Product
        fields = '__all__'


class AddForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control'
    }))
    count = forms.IntegerField(label='Count', widget=forms.NumberInput(attrs={
        'class': 'form-control', 'placeholder': 'Count'
    }))

    class Meta:
        model = Product
        fields = ('product', 'count')
