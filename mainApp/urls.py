from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_cart/<int:flower_id>', views.add_cart, name="add-cart"),
    path('remove_cart/<int:cart_item_id>', views.remove_cart, name="remove-cart"),
    path('update_cart/<int:flower_id>', views.update_cart, name='update-cart'),
    path('account', views.account, name='account'),
    path('search', views.search, name='search'),
    path('view_cart', views.view_cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('checkout_form', views.checkout, name="checkout_form"),
    path('flower/<int:flower_id>', views.flower, name="flower"),
    path('flowers', views.flowers, name="flowers"),
    path('category/<str:category_name>', views.category, name='category'),
    path('flower/<int:flower_id>/payment', views.payment, name="payment"),
    path('view_wish_list', views.view_wish_list, name="wish-list"),
    path('add_wishlist/<int:wishlist_item_id>', views.add_wish_list, name="add-wishlist"),
    path('remove_wish_list/<int:wishlist_item_id>', views.remove_wish_list, name="remove-wishlist"),
    
    # path('signup', views.signup),
]
