from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('powder', 'Powder'),
        ('veg', 'Vegetarian'),
        ('nonveg', 'Non-Vegetarian'),
        ('sweets', 'Sweets'),
        ('chats', 'Chats'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/',blank=True,null=True)
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, null=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Allow null for user
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Remove default to avoid issues
    comment = models.TextField(default='')
    rating = models.IntegerField(null=True)  # Allow null for rating

    def __str__(self):
        return f'{self.user.username if self.user else "Anonymous"} - {self.product.name}'

# In your views.py or wherever your view logic is
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Feedback
from .forms import FeedbackForm

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    feedbacks = Feedback.objects.filter(product=product)
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.product = product
            feedback.user = request.user
            feedback.save()
            return redirect('product_detail', pk=product.pk)
    else:
        form = FeedbackForm()
    
    return render(request, 'product_detail.html', {'product': product, 'feedbacks': feedbacks, 'form': form})
