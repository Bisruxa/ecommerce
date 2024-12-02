from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from products.models import Product
from products.models import Catagory
from orders.models import Order

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'username', 'email']
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'
class CatagorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Catagory
    fields = ("id","name")
class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ("id","status")