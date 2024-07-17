from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/feedback/', views.add_feedback, name='add_feedback'),
    path('veg/', views.veg_products, name='veg_products'),
    path('nonveg/', views.nonveg_products, name='nonveg_products'),
    path('chats/', views.chats_products, name='chats_products'),
    path('sweets/', views.sweets_products, name='sweets_products'),
    path('powder/', views.powder_products, name='powder_products'),
    path('register/', views.register, name='register'),
    path('search/', views.search, name='search'),
    path('search/suggest/', views.suggest_products, name='suggest_products'),
    path('search/suggest/', views.suggest_products, name='suggest_products'),
]
