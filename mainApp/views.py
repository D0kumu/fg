from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.http import Http404
from .models import Flower, Orders, Cart, Payment, Category, Wishlist
from django.contrib.auth.models import User
from django.contrib import messages
import random

# Create your views here.

def home(request):
    current_user = request.session.get('current_user') 
    # print(current_user)
    category = Category.objects.all()
    flowers = Flower.objects.all()
    carts = Cart.objects.filter(user=current_user)
    carts_length = len(carts)
    wishlist = Wishlist.objects.filter(user=current_user)
    wish_list_length = len(wishlist)
    # get the new arrival 
    flowers_list = []
    
    for flower in flowers:
        flowers_list.append(flower)
        flowers_list_minus4 =  len(flowers_list)-4
        new_arivals = flowers_list[flowers_list_minus4:]

        # get the recomended flowers
        recommended_flower = random.choice(flowers_list)
        flowers_list.append(recommended_flower)
        flowers_list_minus4 =  len(flowers_list)-4
        recommended_flowers_list = flowers_list[flowers_list_minus4:]
    
    #get the current logged in user from the session
    
    if 'current_user' in request.session:
        current_user = request.session.get('current_user')
        # print("**************", current_user)
    return render(request, 'main/home.html', {'current_user': current_user, "flowers": flowers ,"carts_length": carts_length, "wish_list_length":wish_list_length, "categories": category, "new_arivals": new_arivals,"recommended_flowers_list":recommended_flowers_list})

def category(request, category_name):
    current_user = request.session.get('current_user') 
    category = Category.objects.filter(name=category_name).first()
    carts = Cart.objects.filter(user=current_user)
    carts_length = len(carts)
    wishlist = Wishlist.objects.filter(user=current_user)
    wish_list_length = len(wishlist)
    category_list = []
    new_flowers = Flower.objects.filter(category=category)
    for flower in new_flowers:
        category_list.append(flower)
    return render(request, 'main/category.html', {"category_list":new_flowers,"carts_length": carts_length, "wish_list_length":wish_list_length,})

def flower(request, flower_id):
    current_user = request.session.get('current_user')
    carts = Cart.objects.filter(user=current_user)
    carts_length = len(carts)
    wishlist = Wishlist.objects.filter(user=current_user)
    wish_list_length = len(wishlist)
    try:
        f = Flower.objects.get(pk=flower_id)
    except Flower.DoesNotExist:
        raise Http404("Flower does not exist")

    return render(request, 'main/flower.html', {"flower": f,"carts_length": carts_length, "wish_list_length":wish_list_length,})

def flowers(request):
    category_list = []
    current_user = request.session.get('current_user') 
    f = Flower.objects.all()
    carts = Cart.objects.filter(user=current_user)
    carts_length = len(carts)
    wishlist = Wishlist.objects.filter(user=current_user)
    wish_list_length = len(wishlist)
    categories = Category.objects.all()

    for ct in categories:
        new_flowers = Flower.objects.filter(category=ct)
        for flower in new_flowers:
            category_list.append(flower)
    
        for flower in category_list:
            obj = {"category":flower.category.name, "flower": flower.name}
                                                 
    return render(request, 'main/shop.html', {"flowers": f,"carts_length": carts_length, "categories":categories , "wish_list_length":wish_list_length,})

def checkout(request):

    return render(request, 'main/checkout.html')

def wish_list(request):
    return render(request, 'main/wishlist.html')

def search(request):
    if request.method == "POST":
        seach_text = request.POST['search']
        print(seach_text)
        flower = Flower.objects.filter(name=str(seach_text))
        print(flower)
        return HttpResponse(seach_text)
    

def checkout_form(request):
    if request.method == "POST":
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]
        email = request.POST["email"]
        company = request.POST["company"]
        region = request.POST["region"]
        adress = request.POST["address"]
        city = request.POST["city"]
        phone = request.POST["phone"]

        newOrders = Orders(first_name=first_name, 
                           last_name=last_name, 
                           email=email, 
                           company=company,
                           region=region,
                           city=city,
                           adress=adress,
                           phone=phone,
                           )
        newOrders.save()
    return render(request, 'checkout.html')

def checkout(request):
    user = request.user
    carts = Cart.objects.filter(user=user.id)
    cart_prices = []
    for cart_item in carts:
        cart_prices.append(cart_item.item.price)
        
    for item in cart_prices:
        sub_total = sum(cart_prices)
       
    return render(request, 'main/checkout.html', {'sub_total':sub_total,"total":sub_total+100})

def add_cart(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)
    Cart.objects.get_or_create(user=request.user, item=flower)
    
    messages.success(request, "Your cart has been added successfully ")
    return redirect('home')

def remove_cart(request, cart_item_id):
    flower = get_object_or_404(Flower, pk=cart_item_id)
    cart_item = Cart.objects.filter(user=request.user, item=cart_item_id)
    cart_item.delete()
    messages.success(request, "Your cart has been removed successfully ")
    return redirect('home')

def view_cart(request):
    current_user = request.session.get('current_user') 
    carts = Cart.objects.filter(user=current_user)
    carts_length = len(carts)
    cart_items = Cart.objects.filter(user=request.user)
    for item in cart_items:
       print( item.quantity)

    total_price = sum(i.item.price * i.quantity for i in cart_items)
    return render(request, 'main/cart.html', {'cart_items': cart_items, 'total_price': total_price,"carts_length": carts_length,})

def update_cart(request, flower_id):
    flower = get_object_or_404(Flower, pk=flower_id)
    cart_item = get_object_or_404(Cart, item=flower)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        if quantity > 1:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart')

def add_wish_list(request, wishlist_item_id):
    flower = get_object_or_404(Flower, pk=wishlist_item_id)
    Wishlist.objects.get_or_create(user=request.user, item=flower)
    
    messages.success(request, "You have successfully added a flower to your Wishlist  ")
    return redirect('home')

def remove_wish_list(request, wishlist_item_id):
    flower = get_object_or_404(Flower, pk=wishlist_item_id)
    wish_list_item = Wishlist.objects.filter(user=request.user, item=wishlist_item_id)
    wish_list_item.delete()
    messages.success(request, "Your wishlist item has been removed successfully ")
    return redirect('home')

def view_wish_list(request):
    current_user = request.session.get('current_user') 
    wishlist = Wishlist.objects.filter(user=current_user)
    carts = Cart.objects.filter(user=current_user)
    carts_length = len(carts)
    wish_list_length = len(wishlist)
    wish_list_items = Wishlist.objects.filter(user=request.user)
    for item in wish_list_items:
       print( item)

    # total_price = sum(i.item.price * i.quantity for i in wish_list_items)
    return render(request, 'main/wishlist.html', {'wish_list_items': wish_list_items,"wish_list_length":wish_list_length, "carts_length":carts_length})


def account(request):
    user = request.user
    current_user = request.session.get('current_user') #this is redundancy I know!!
    carts = Cart.objects.filter(user=current_user)
    carts_length = len(carts)
    return render(request, 'main/account.html', {"user":user,"carts_length": carts_length})

def payment(request, flower_id):

    return render(request, 'main/payment.html', {"payments":Payment.objects.all() })