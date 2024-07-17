from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product, Feedback
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()

    # Categorize products
    categories = {
        'veg': products.filter(category='veg'),
        'nonveg': products.filter(category='nonveg'),
        'sweets': products.filter(category='sweets'),
        'chats': products.filter(category='chats'),
        'powder': products.filter(category='powder'),
    }
    
    return render(request, 'products/product_list.html', {'categories': categories, 'query': query})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    feedbacks = Feedback.objects.filter(product=product)
    return render(request, 'products/product_detail.html', {'product': product, 'feedbacks': feedbacks})

def veg_products(request):
    products = Product.objects.filter(category='veg')
    return render(request, 'products/veg.html', {'products': products})

def nonveg_products(request):
    products = Product.objects.filter(category='nonveg')
    return render(request, 'products/nonveg.html', {'products': products})

def chats_products(request):
    products = Product.objects.filter(category='chats')
    return render(request, 'products/chats.html', {'products': products})

def sweets_products(request):
    products = Product.objects.filter(category='sweets')
    return render(request, 'products/sweets.html', {'products': products})
def powder_products(request):
    products = Product.objects.filter(category='powder')
    return render(request, 'products/powders.html', {'products': products})

@login_required
def add_feedback(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        comment = request.POST['comment']
        rating = request.POST['rating']
        Feedback.objects.create(user=request.user, product=product, comment=comment, rating=rating)
    return redirect('product_detail', pk=product.pk)

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def search(request):
    query = request.GET.get('query', '')
    allproducts = Product.objects.filter(name__icontains=query)
    
    # Filter categories dynamically based on matching products
    categories = ['veg', 'nonveg', 'sweets', 'chats']
    available_categories = []
    
    for category in categories:
        if Product.objects.filter(category=category, name__icontains=query).exists():
            available_categories.append(category)
    
    output = {
        'allproducts': allproducts,
        'query': query,
        'available_categories': available_categories,
    }
    
    return render(request, 'search.html', output)

from django.http import JsonResponse
from .models import Product

def suggest_products(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(name__icontains=query)[:5]  # Limiting to 5 suggestions
    suggestions = [product.name for product in products]
    return JsonResponse({'suggestions': suggestions})

