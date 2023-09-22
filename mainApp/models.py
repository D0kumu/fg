from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Category(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to ='static/uploads/%Y/%m/%d/')
    added_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class Flower(models.Model):
    name = models.CharField(default=None, max_length=200)
    scientific_name = models.CharField(default=None, max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to ='static/uploads/%Y/%m/%d/')
    out_of_stock = models.BooleanField(default=False)
    added_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.name

class Orders(models.Model):
    first_name = models.CharField(default=None, max_length=200)
    last_name = models.CharField(default=None, max_length=200)
    email = models.CharField(default=None, max_length=200)
    phone = models.CharField(default=None, max_length=200)
    company = models.CharField(default=None, max_length=200)
    region = models.CharField(default=None, max_length=200)
    city = models.CharField(default=None, max_length=200)
    adress = models.CharField(default=None, max_length=200)
    order_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.id
    
class Cart(models.Model):
    item = models.ForeignKey(Flower, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.item.name
    
class Wishlist(models.Model):
    item = models.ForeignKey(Flower, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    cart_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.item.name

class Payment(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    amount_payed = models.IntegerField()
    payer = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.order.item.name
